# Bot de Monitoramento de Câmbio diário + Relatório (USD_BRL)

Um aplicativo simples de monitoramento de câmbio utilizando python.

## Descrição

Este projeto é um bot que realiza o monitoramento de câmbio USD - BRL com as seguintes funcionalidades:
- **Acessa um site de câmbio**
- **Coleta o valor do dólar para o dia atual**
- **Coleta a data da cotação**
- **Especifica o site de onde foi coletada a informação**
- **Realiza um print da página acessada**
- **Armazena os dados em um arquivo .docx**
- **Converte o arquivo .docx para .pdf**
- **Entrega os arquivos na sua área de trabalho**


## Requisitos

- Python 3.7 ou superior

## Instalação

1. **Clone este repositório:**

    ```bash
    git clone https://github.com/cadumrod/bot_cambio_USD_BRL
    cd bot_cambio_USD_BRL
    ```

2. **Crie e ative um ambiente virtual:**

    No Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    No macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Construa o executável com `cx_Freeze`**:

    ```bash
    python setup.py build
    ```

## Uso

1. Após a construção, o executável estará disponível no diretório `build`. Para executar o aplicativo, navegue até o diretório de saída (por exemplo, `build/exe.win-amd64-3.12` no Windows) e execute o arquivo gerado:

    No Windows:
    ```bash
    cd build/exe.win-amd64-3.12
    app.exe
    ```

    No macOS/Linux:
    ```bash
    cd build/exe.macosx-10.6-intel-3.12
    ./app
    ```

## Instalador

Caso prefira, baixe o instalador diretamente do repositório:

- [Instalador](./installer/MonitoramentoSetup.exe)

Após baixar, execute o instalador e siga as instruções na tela.

## Estrutura do Projeto

- `app.py`: Arquivo principal do aplicativo.
- `hyperlink.py`: Contém a função para criar o hyperlink do site de câmbio.
- `business.ico`: Ícone usado no aplicativo.
- `setup.py`: Script de instalação e configuração do projeto.
- `MonitoramentoSetup.exe`: Instalador da aplicação que se encontra dentro da pasta "installer" deste repositório.
- `README.md`: Este arquivo de documentação.
- `requirements.txt`: Arquivo de requisitos com as dependências do projeto.
- `LICENSE`: Licença MIT.


## Autor

**Carlos Rodrigues**

- [GitHub](https://github.com/cadumrod)
- [E-mail](mailto:carlosrod.dev@gmail.com)

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.