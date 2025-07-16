# MedFile Parser and HTML Viewer

Este repositório contém o parser de referência para o **MedFile**, um formato de texto simplificado e legível por humanos para criar e compartilhar anotações médicas.

Além do parser, este projeto agora inclui um **Visualizador HTML** interativo que permite:

*   Visualizar arquivos `.med` formatados diretamente no navegador.
*   Baixar o conteúdo formatado como um arquivo HTML.
*   Utilizar um "Modo Apresentação" para exibir o documento em tela cheia, ideal para reuniões e compartilhamento.

Para a especificação completa do formato MedFile, exemplos detalhados, o roadmap de desenvolvimento do parser e instruções completas sobre o visualizador HTML, por favor, consulte o arquivo [medfile.md](medfile.md).

## Como Começar (Visualizador HTML)

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/andremillet/medfile.git
    cd medfile
    ```

2.  **Abra o visualizador:**

    Simplesmente abra o arquivo `index.html` no seu navegador web preferido.

3.  **Selecione um arquivo .med:**

    Clique em "Selecionar Arquivo .med" e escolha um dos arquivos de exemplo (ex: `example.med` ou `JMC.med`) ou qualquer outro arquivo `.med` que você tenha.

## Como Começar (Parser Python)

Para usar o parser Python (Fase 1 concluída):

1.  **Certifique-se de ter Python 3 instalado.**
2.  **Execute o parser:**
    ```bash
    python3 main.py
    ```
    O script irá processar o `example.med` e imprimir a saída em formato JSON no console.

## Como Contribuir

Sinta-se à vontade para abrir *issues* ou enviar *pull requests*. O [roadmap de desenvolvimento](medfile.md#roadmap) é um ótimo lugar para começar a procurar as próximas tarefas.