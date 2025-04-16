Este projeto implementa um pipeline de dados para processar leituras de temperatura provenientes de dispositivos IoT, utilizando Docker para gerenciar um contêiner PostgreSQL, Python para o processamento dos dados e Streamlit para a criação de um dashboard interativo.
Desenvolvi como projeto da disciplina de Arquiteturas Disruptivas, explorando conceitos de IoT, Big Data e Inteligência Artificial.

Visão Geral
O objetivo do projeto é:

Ler e processar dados de temperatura provenientes de dispositivos IoT (arquivo CSV).
Inserir os dados processados em uma instância do PostgreSQL rodando em um contêiner Docker.
Desenvolver um dashboard com Streamlit e Plotly para visualização dos dados.

Pré-requisitos
Python 3.8 ou superior
Docker instalado (Docker Desktop)

Configuração e Instalação
1. Clonar o Repositório
git clone https://github.com/salanmato/04_iot_bigdata_ia.git
cd 04_iot_bigdata_ia

2. Instalar as Dependências Python
pip install pandas psycopg2-binary sqlalchemy streamlit plotly
as dependencias estão todas no requirements.txt  a execução do compose faz as instalações dentro o conteiner

3. Configurar o Contêiner PostgreSQL com Docker
Execute o seguinte comando para iniciar o contêiner PostgreSQL:

docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres
Nota: Substitua sua_senha pela senha desejada.

foi criado um serviço no docker-compose que cria o conteiner junto 

Executando o Projeto
1. Crie o banco de dados e tabela
Conecte-se ao PostgreSQL (via psql, pgAdmin ou outro cliente SQL) e execute os comandos para criar as views. Por exemplo:

( como fiz via DBEAVER, ele já joga a table dentro da Database do postgres )
create table temp_notes(
id VARCHAR(100),
temp INTEGER,
out_in VARCHAR(5),
noted_date DATE,
room VARCHAR(20)
)


2. Para iniciar o dashboard, execute:

streamlit run app.py
