import argparse
import os
import sys
import logging
from datetime import datetime

# Configuração básica do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_med_file(file_path):
    """
    Analisa um arquivo .med para extrair os metadados necessários.

    Args:
        file_path (str): O caminho para o arquivo .med.

    Returns:
        dict: Um dicionário contendo os metadados encontrados.
    """
    metadata = {
        "identificador_paciente": None,
        "identificador_atendente": None,
        "criado_em": None
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                cleaned_line = line.strip()
                if cleaned_line.startswith('identificador_paciente'):
                    metadata['identificador_paciente'] = cleaned_line.split(':', 1)[1].strip()
                elif cleaned_line.startswith('identificador_atendente'):
                    metadata['identificador_atendente'] = cleaned_line.split(':', 1)[1].strip()
                elif cleaned_line.startswith('criado_em'):
                    metadata['criado_em'] = cleaned_line.split(':', 1)[1].strip()
    except FileNotFoundError:
        logging.error(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Ocorreu um erro ao ler o arquivo: {e}")
        sys.exit(1)
        
    return metadata

def main():
    """
    Função principal para validar e renomear o arquivo .med.
    """
    parser = argparse.ArgumentParser(
        description="Valida e renomeia arquivos .med com base nos metadados internos."
    )
    parser.add_argument("file_path", help="O caminho para o arquivo .med a ser processado.")
    args = parser.parse_args()

    file_path = args.file_path

    if not os.path.exists(file_path):
        logging.error(f"Erro: O caminho '{file_path}' não existe.")
        sys.exit(1)

    metadata = parse_med_file(file_path)

    # Validação dos metadados
    missing_tags = []
    if not metadata["identificador_paciente"]:
        missing_tags.append("identificador_paciente")
    if not metadata["identificador_atendente"]:
        missing_tags.append("identificador_atendente")
    if not metadata["criado_em"]:
        missing_tags.append("criado_em")

    if missing_tags:
        for tag in missing_tags:
            logging.warning(f"ALERTA: Metadado obrigatório '{tag}' não encontrado no arquivo.")
        sys.exit(1)

    # Processamento da data e renomeação
    try:
        # Tenta formatos comuns de data e hora
        criado_em_str = metadata["criado_em"]
        dt_object = None
        # Formato: 16/08/2025 13:19:45
        try:
            dt_object = datetime.strptime(criado_em_str, '%d/%m/%Y %H:%M:%S')
        except ValueError:
            # Formato ISO: 2025-08-16 13:19:45
            dt_object = datetime.strptime(criado_em_str, '%Y-%m-%d %H:%M:%S')

        new_filename = dt_object.strftime('%Y-%m-%d_%H%M%S') + '.med'
        
        directory = os.path.dirname(file_path)
        old_filename = os.path.basename(file_path)
        new_file_path = os.path.join(directory, new_filename)

        if os.path.exists(new_file_path):
            logging.warning(f"O arquivo de destino '{new_filename}' já existe. A operação foi cancelada.")
            sys.exit(1)

        os.rename(file_path, new_file_path)
        logging.info(f"Arquivo '{old_filename}' renomeado para '{new_filename}' com sucesso.")

    except ValueError:
        logging.error(f"Erro ao converter a data '{metadata['criado_em']}'. Formato esperado: 'DD/MM/AAAA HH:MM:SS' ou 'AAAA-MM-DD HH:MM:SS'.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Ocorreu um erro ao renomear o arquivo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
