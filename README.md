<b>Este README esá em inglês e português<br></b>
<b>This README is in english and portuguese</b>

# 🤖 RPA extrair relatório e inserir no banco de dados

## Descrição

O projeto desenvolvido em Python, é focado na extração de dados de fontes externas e inserção automatizada desses dados em um banco de dados.  
Ideal para tarefas rotineiras de coleta, transformação e armazenamento de dados, reduzindo erros manuais e acelerando processos repetitivos.

## ✨ Como funciona

- Automatiza a coleta de dados.
- Realiza o tratamento e processamento dos dados extraídos.
- Insere os dados automaticamente em um banco de dados.
- Possui logs para acompanhamento do fluxo e tratamento de erros.


## 🛠️ Bibliotecas Utilizadas

O projeto faz uso principalmente de bibliotecas padrão e populares do Python para automação e manipulação de dados, tais como:

- 🕹️ **Selenium**: automação de navegador.
- 🗂️ **Pandas**: manipulação de dados tabulares.
- 🛢️ **sqlite3** ou **SQLAlchemy**: conexão e manipulação de banco de dados.
- 📝 **logging**: geração de logs do processo.
- 📦 Outras utilidades descritas em `requirements.txt`.

*Consulte o arquivo [`requirements.txt`](./requirements.txt) para a lista completa de dependências.*

## 📁 Estrutura dos Arquivos

- `main.py`: ponto de entrada do projeto.
- `extrair_dados.py`: funções para extração e tratamento de dados.
- `config/`: arquivos de configuração (ex: acesso ao banco, parâmetros de execução).
- `logs/`: diretório para arquivos de log do processo.
- `requirements.txt`: lista de dependências do projeto.


## ⚠️ Observações

- Os caminhos e parâmetros podem estar configurados para ambiente Windows, ajuste conforme necessário.
- Certifique-se de instalar todas as dependências com `pip install -r requirements.txt`.
- Configure corretamente o acesso ao banco de dados no arquivo de configuração.
- O projeto pode exigir drivers específicos para o banco de dados utilizado.

## ▶️ Exemplo de execução

```bash
python main.py
```

Todo o processo será registrado em arquivos de log para acompanhamento.

<br>

# 🤖 RPA Extract Report and Insert into Database

## Description

This project, developed in Python, focuses on extracting data from external sources and automatically inserting that data into a database.  
It is ideal for routine tasks involving data collection, transformation, and storage—reducing manual errors and speeding up repetitive processes.

## ✨ How it works

- Automates data collection from external sources.
- Processes and transforms the extracted data.
- Automatically inserts the processed data into a database.
- Includes logging for workflow tracking and error handling.

## 🛠️ Libraries Used

The project mainly uses standard and popular Python libraries for automation and data manipulation, such as:

- 🕹️ **Selenium**: browser automation.
- 🗂️ **Pandas**: tabular data manipulation.
- 🛢️ **sqlite3** or **SQLAlchemy**: database connection and manipulation.
- 📝 **logging**: process logging.
- 📦 Other utilities described in `requirements.txt`.

*See the [`requirements.txt`](./requirements.txt) file for the full list of dependencies.*

## 📁 File Structure

- `main.py`: project entry point.
- `extrair_dados.py`: functions for data extraction and processing.
- `config/`: configuration files (e.g., database access, execution parameters).
- `logs/`: directory for process log files.
- `requirements.txt`: list of project dependencies.

## ⚠️ Notes

- File paths and parameters may be set for a Windows environment—adjust as needed for your setup.
- Make sure to install all dependencies with `pip install -r requirements.txt`.
- Properly configure database access in the configuration file.
- The project may require specific drivers for the chosen database.

## ▶️ Example of execution

```bash
python main.py
```

The entire process will be logged for tracking and auditing purposes.
