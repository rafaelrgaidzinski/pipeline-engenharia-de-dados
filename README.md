# Pipeline de Engenharia de Dados com Airflow + PostgreSQL

📌 Objetivo

Este projeto tem como objetivo construir um pipeline de dados que realiza:
1. Leitura de arquivos .csv
2. Carga em um banco de dados PostgreSQL
3. Orquestração da ingestão via Airflow
4. Base para um modelo dimensional que será consumido por dashboards


🏗️ Estrutura do 

pipeline-engenharia-de-dados/
├── airflow/
│   ├── dags/
│   ├── logs/
│   ├── plugins/
│   └── docker-compose.yml
├── data/
│   ├── customers.csv
│   ├── orders.csv
│   └── ...demais CSVs
├── scripts/
│   └── populate_postgres.py
├── .env
└── README.


⚙️ Pré-requisitos

1. Docker e Docker Compose instalados
2. Python 3.12 (caso deseje rodar os scripts fora do Airflow)
3. psycopg2, pandas, sqlalchemy, python-dotenv

🐘 Subindo PostgreSQL e Airflow

1. Criação do container PostgreSQL (caso queira isolado):
docker run -d \
  --name postgres \
  -e POSTGRES_USER=airflow \
  -e POSTGRES_PASSWORD=airflow \
  -e POSTGRES_DB=airflow \
  -p 5432:5432 \
  postgres:
  
2. Subindo o ambiente Airflow com PostgreSQL:
2.1. Dentro da pasta airflow/, execute:
export AIRFLOW_UID=$(id -u)
docker compose up airflow-init
docker compose up -d

2.2. O Airflow será exposto em: http://localhost:8080
Credenciais padrão:
Usuário: admin
Senha: admin

📥 Populando o PostgreSQL com os arquivos CSV

Execute o script scripts/popular_postgre.py:
python scripts/populate_postgres.py

Esse script: 
- Lê os arquivos .csv da pasta data/
- Cria automaticamente as tabelas no banco PostgreSQL
- Insere os dados via SQLAlchemy

🔄 Acessando o banco PostgreSQL no terminal (WSL ou Linux)

docker exec -it postgres psql -U airflow -d airflow