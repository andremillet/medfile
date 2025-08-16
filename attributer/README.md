# Attributer

`attributer` é uma ferramenta de linha de comando projetada para validar e padronizar arquivos de registros médicos no formato `.med`.

## Funcionalidades

O programa analisa um arquivo `.med` para garantir que ele contenha os metadados essenciais antes de ser processado por outras ferramentas do sistema.

O fluxo de trabalho principal é:

1.  **Receber um arquivo:** Aceita o caminho para um arquivo `.med` como argumento.
2.  **Validar Metadados:** Verifica a presença das três tags obrigatórias:
    *   `identificador_paciente` (CPF do paciente)
    *   `identificador_atendente` (CRM do médico/atendente)
    *   `criado_em` (Data e hora de criação do registro)
3.  **Alertar sobre Falhas:** Se qualquer uma das tags estiver ausente, o programa exibe um alerta e encerra a execução sem modificar o arquivo.
4.  **Renomear em Caso de Sucesso:** Se todas as tags estiverem presentes, o programa extrai a data e hora de `criado_em` e renomeia o arquivo no mesmo diretório para o formato padronizado `AAAA-MM-DD_HHMMSS.med`.

Essa ferramenta garante que apenas arquivos completos e bem-formados sigam no fluxo de processamento de dados médicos.
