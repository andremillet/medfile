# MedFile: Um Formato Simplificado para Registros Médicos

## Visão Geral

O **MedFile** foi concebido para ser um formato de texto simples e legível por humanos para criar e compartilhar anotações médicas. O objetivo é facilitar a rápida compreensão da avaliação clínica por múltiplos profissionais e permitir a integração com prontuários eletrônicos de forma menos verbosa e mais estruturada.

Por ser um arquivo de texto puro (a sugestão é usar a extensão `.med`), ele pode ser criado e editado em qualquer editor de texto (como Notepad, Gedit, VSCode, Vim, etc.). A sua visualização e estilização podem ser otimizadas por softwares especializados que interpretam (parse) sua estrutura.

## Estrutura do Documento

Um documento MedFile é organizado em seções principais, cada uma indicada por um título entre colchetes `[]`.

### `[ANAMNESE]`

Esta seção contém a apresentação do quadro clínico do paciente, incluindo a queixa principal e informações estruturadas através de tags especiais.

-   **Queixa Principal**: Um texto livre descrevendo o motivo da consulta.
-   **Tags Especiais**: A anamnese utiliza tags iniciadas com `!` para detalhar informações:
    -   `!HPP`: **História Patológica Pregressa**. Lista os diagnósticos ou condições prévias do paciente.
        -   *Exemplo:* `!HPP HAS; DM; HIPOTIREOIDISMO;`
    -   `!MED`: **Medicações em Uso**. Relação de medicamentos que o paciente utiliza.
        -   *Formato:* `NOME-DA-MEDICACAO DOSE [OBSERVAÇÕES] POSOLOGIA`
        -   *Exemplo:* `!MED AMITRIPTILINA 25MG NOITE;`
        -   *Exemplo com observação:* `!MED AMITRIPTILINA 25MG [2 COMPRIMIDOS] NOITE;`
    -   `!HF`: **História Familiar**. Registra informações familiares relevantes para o quadro.
        -   *Exemplo:* `!HF NEGA;`
    -   `!RX`: **Resultados de Exames**. Lista os resultados de exames complementares relevantes.
        -   *Formato:* `@NOME_DO_EXAME[DATA_OPCIONAL]: RESULTADO`
        -   *Exemplo:* `@LAB[05/2025]: B12 100; TSH 25;`
        -   *Exemplo:* `@RM_CRANIO[05/2025]: microangiopatia fazekas 3;`
    -   `!!`: **Observações Adicionais**. Usado para notas de retorno ou adendos à história inicial.
        -   *Exemplo:* `!! Já em atividade fisica regular`
        -   *Exemplo com marcador de tempo:* `!! Já em acompanhamento psicologico[6m]`

### `[EXAME FISICO]`

Esta seção descreve os achados relevantes observados durante o exame físico do paciente.

### `[HIPOTESE DIAGNOSTICA]`

Lista as hipóteses diagnósticas, idealmente utilizando uma terminologia clara e, se possível, alinhada à classificação CID-10.

-   *Exemplo:* `Transtorno Cognitivo Leve`
-   *Exemplo:* `Sequela de Acidente Vascular Encefalico`

### `[CONDUTA]`

Esta seção funciona como um conjunto de comandos ou tarefas a serem executadas, especialmente em relação à terapêutica e ao plano de cuidados.

-   **Modificação de Medicação**:
    -   `+`: **Adicionar** uma nova medicação.
        -   *Exemplo:* `+GALANTAMINA 4MG;`
    -   `++`: **Incrementar** a dose de uma medicação existente.
        -   *Exemplo:* `++GALANTAMINA 8MG;`
    -   `-`: **Suspender** uma medicação.
        -   *Exemplo:* `-ALPRAZOLAM;`
    -   `--`: **Decrementar** a dose de uma medicação.
-   **Planejamento Futuro**:
    -   `>>`: Sinaliza uma **proposta** para avaliações futuras, geralmente após uma conduta.
        -   *Exemplo:* `+CLONAZEPAM 2,5MG/ML [5 GOTAS] NOITE >> !desmame` (aqui, `!desmame` é uma palavra-chave que sinaliza a intenção de retirada progressiva).
-   **Outras Condutas**:
    -   Descritas em texto livre, preferencialmente em primeira pessoa.
    -   *Exemplo de encaminhamento:* `Encaminho para acompanhamento com Psicologia.`
    -   *Exemplo de solicitação:* `Solicito RM de cranio.`

---

## Exemplo de Documento Completo

Abaixo, um exemplo de como um documento `.med` seria na prática.

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
