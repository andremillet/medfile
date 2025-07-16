# MedFile: Um Formato Simplificado para Registros Médicos

## Visão Geral

O **MedFile** foi concebido para ser um formato de texto simples e legível por humanos para criar e compartilhar anotações médicas. O objetivo é facilitar a rápida compreensão da avaliação clínica por múltiplos profissionais e permitir a integração com prontuários eletrônicos de forma menos verbosa e mais estruturada.

Este documento serve como a especificação oficial do formato e a documentação central do projeto do parser de referência.

## Estrutura do Documento MedFile

Um documento MedFile é organizado em seções principais, cada uma indicada por um título entre colchetes `[]`.

### `[ANAMNESE]`

Contém a apresentação do quadro clínico do paciente.

-   **Queixa Principal**: Um texto livre descrevendo o motivo da consulta.
-   **Tags Especiais**: A anamnese utiliza tags iniciadas com `!` para detalhar informações:
    -   `!HPP`: História Patológica Pregressa.
    -   `!MED`: Medicações em Uso.
    -   `!HF`: História Familiar.
    -   `!RX`: Resultados de Exames.
    -   `!!`: Observações Adicionais.

### `[EXAME FISICO]`

Descreve os achados relevantes observados durante o exame físico.

### `[HIPOTESE DIAGNOSTICA]`

Lista as hipóteses diagnósticas.

### `[CONDUTA]`

Funciona como um conjunto de comandos ou tarefas a serem executadas.

---

## Desenvolvimento do Parser

Para dar vida ao formato MedFile, estamos desenvolvendo um parser de referência em Python. O objetivo é ler um arquivo `.med` e convertê-lo em um formato estruturado (JSON), facilitando a sua utilização por outros sistemas.

### Roadmap

-   [x] **Fase 1: Parser Básico de Seções e Anamnese**
    -   [ ] **Fase 2:** Implementar o parsing detalhado das tags `!MED` e `!RX`.
    -   [ ] **Fase 3:** Implementar o parsing da seção `[CONDUTA]` para extrair ações.
    -   [ ] **Fase 4:** Criar uma ferramenta de linha de comando (CLI).
    -   [ ] **Fase 5:** Adicionar suporte para output em outros formatos (ex: HTML).

### Como Executar o Projeto

Para que outro desenvolvedor ou LLM possa replicar e continuar o trabalho, siga os passos abaixo.

1.  **Crie o arquivo `example.med`:**

    ```medfile
    [ANAMNESE]
    PACIENTE COM QUEIXAS DE PREJUIZO DE MEMORIA EPISODICA, COM PREDOMINIO DE FATOS RECENTES E MENÇÃO DE PREJUIZO SIGNIFICATIVO EM FUNÇÕES EXECUTIVAS, COMPROMETENDO ATIVIDADES BASICAS E INSTRUMENTAIS, EM CARÁTER PROGRESSIVO, HÁ 6 ANOS.

    !HPP HAS; DM; HIPOTIREOIDISMO;
    !MED LOSARTANA 50MG 12/12 HORAS; METFORMINA 500MG [LIBERACAO CONTROLADA, 2 COMPRIMIDOS] MANHA NOITE; ALPRAZOLAM 2MG NOITE;
    !HF NEGA;
    !RX @RM_CRANIO[05/2025]: FAZEKAS 3; MTA 3;
    !RX @LAB[05/2025]: B12 100; TSH 25;

    [EXAME FISICO]
    DESORIENTADO EM TEMPO E ESPAÇO;
    PARCIALMENTE COOPERATIVO;

    [HIPOTESE DIAGNOSTICA]
    DEMENCIA NA DOENÇA DE ALZHEIMER
    DEMENCIA VASCULAR?
    HIPOVITAMINOSE
    HIPOTIREOIDISMO
    INTOXICAÇÃO EXOGENA

    [CONDUTA]
    +AAS 100MG ALMOÇO;
    +SINVASTATINA 20MG NOITE;
    +GALANTAMINA 4MG;
    +MECOBALAMINA 1000MCG;
    -ALPRAZOLAM;
    +CLONAZEPAM 2,5MG/ML [5 GOTAS] NOITE >> !DESMAME
    ORIENTO ATIVIDADE FISICA REGULAR
    ```

2.  **Crie e execute o parser `main.py`:**

    ```python
    import re
    import json

    def parse_med_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        data = {}
        sections = re.split(r'\n(?=\[[A-Z\s]+\])', content)

        for section in sections:
            section = section.strip()
            if not section:
                continue

            header_match = re.match(r'\[([A-Z\s]+)\]', section)
            if header_match:
                header = header_match.group(1)
                section_content = section[len(header)+2:].strip()
                data[header] = parse_section_content(header, section_content)
            else:
                if 'unstructured' not in data:
                    data['unstructured'] = ''
                data['unstructured'] += section + '\n'

        return data

    def parse_section_content(header, content):
        if header == "ANAMNESE":
            return parse_anamnese(content)
        return content.split('\n')

    def parse_anamnese(content):
        anamnese_data = {'queixa_principal': ''}
        lines = content.split('\n')
        
        queixa_principal_lines = []
        for line in lines:
            if line.startswith('!'):
                tag_match = re.match(r'!([A-Z]+) (.*)', line)
                if tag_match:
                    tag, value = tag_match.groups()
                    anamnese_data[tag.lower()] = [v.strip() for v in value.split(';') if v.strip()]
            else:
                queixa_principal_lines.append(line)
        
        anamnese_data['queixa_principal'] = '\n'.join(queixa_principal_lines).strip()
        return anamnese_data

    if __name__ == "__main__":
        parsed_data = parse_med_file('example.med')
        print(json.dumps(parsed_data, indent=4, ensure_ascii=False))
    ```

3.  **Resultado Esperado (Saída do Parser):**

    ```json
    {
        "ANAMNESE": {
            "queixa_principal": "PACIENTE COM QUEIXAS DE PREJUIZO DE MEMORIA EPISODICA...",
            "hpp": [
                "HAS",
                "DM",
                "HIPOTIREOIDISMO"
            ],
            "med": [
                "LOSARTANA 50MG 12/12 HORAS",
                "METFORMINA 500MG [LIBERACAO CONTROLADA, 2 COMPRIMIDOS] MANHA NOITE",
                "ALPRAZOLAM 2MG NOITE"
            ],
            "hf": [
                "NEGA"
            ],
            "rx": [
                "@LAB[05/2025]: B12 100",
                "TSH 25"
            ]
        },
        "EXAME FISICO": [...],
        "HIPOTESE DIAGNOSTICA": [...],
        "CONDUTA": [...]
    }
    ```