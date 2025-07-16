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

## Visualizador HTML

Um visualizador HTML foi desenvolvido para permitir a fácil visualização e apresentação de arquivos `.med` diretamente no navegador. Ele inclui um parser JavaScript embutido que interpreta o formato MedFile e o renderiza com estilos modernos, além de um "Modo Apresentação" para exibição otimizada.

### Como Usar o Visualizador

1.  Abra o arquivo `index.html` em qualquer navegador web.
2.  Clique em "Selecionar Arquivo .med" e escolha um arquivo com a extensão `.med` (ex: `example.med` ou `JMC.med`).
3.  O conteúdo do arquivo será exibido formatado na tela.
4.  **Download HTML Formatado**: Clique no botão "Download HTML Formatado" para baixar o conteúdo exibido como um arquivo HTML.
5.  **Modo Apresentação**: Clique no botão "Modo Apresentação" para entrar no modo de tela cheia, ideal para apresentações. Use os botões "Anterior" e "Próximo" para navegar entre as seções do documento. Para sair, clique no botão "Sair do Modo Apresentação" no canto superior direito.

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
