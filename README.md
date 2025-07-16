# MedFile Parser

Este repositório contém o parser de referência para o **MedFile**, um formato de texto simplificado e legível por humanos para criar e compartilhar anotações médicas.

O objetivo é facilitar a rápida compreensão da avaliação clínica por múltiplos profissionais e permitir a integração com prontuários eletrônicos de forma menos verbosa e mais estruturada.

Para a especificação completa do formato, exemplos detalhados e o roadmap de desenvolvimento, por favor, consulte o arquivo [medfile.md](medfile.md).

## Status Atual

O parser está na **Fase 1** de desenvolvimento, sendo capaz de processar as seções principais de um arquivo `.med` e extrair as informações da seção `[ANAMNESE]`.

## Como Começar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/andremillet/medfile.git
    cd medfile
    ```

2.  **Execute o parser:**

    O script `main.py` irá processar o arquivo `example.med` e imprimir a saída em formato JSON.

    ```bash
    python3 main.py
    ```

3.  **Saída Esperada:**

    ```json
    {
        "ANAMNESE": {
            "queixa_principal": "PACIENTE COM QUEIXAS DE PREJUIZO DE MEMORIA EPISODICA, COM PREDOMINIO DE FATOS RECENTES E MENÇÃO DE PREJUIZO SIGNIFICATIVO EM FUNÇÕES EXECUTIVAS, COMPROMETENDO ATIVIDADES BASICAS E INSTRUMENTAIS, EM CARÁTER PROGRESSIVO, HÁ 6 ANOS.",
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
        "EXAME FISICO": [
            "DESORIENTADO EM TEMPO E ESPAÇO;",
            "PARCIALMENTE COOPERATIVO;"
        ],
        "HIPOTESE DIAGNOSTICA": [
            "DEMENCIA NA DOENÇA DE ALZHEIMER",
            "DEMENCIA VASCULAR?",
            "HIPOVITAMINOSE",
            "HIPOTIREOIDISMO",
            "INTOXICAÇÃO EXOGENA"
        ],
        "CONDUTA": [
            "+AAS 100MG ALMOÇO;",
            "+SINVASTATINA 20MG NOITE;",
            "+GALANTAMINA 4MG;",
            "+MECOBALAMINA 1000MCG;",
            "-ALPRAZOLAM;",
            "+CLONAZEPAM 2,5MG/ML [5 GOTAS] NOITE >> !DESMAME",
            "ORIENTO ATIVIDADE FISICA REGULAR"
        ]
    }
    ```

## Como Contribuir

Sinta-se à vontade para abrir *issues* ou enviar *pull requests*. O [roadmap de desenvolvimento](medfile.md#roadmap) é um ótimo lugar para começar a procurar as próximas tarefas.
