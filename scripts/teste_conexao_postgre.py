from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import sql

# Carrega as variáveis do .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path, override=True)

# Lê as variáveis do ambiente
server = os.getenv("DB_SERVER")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

# print(f"Variáveis carregadas: SERVER={server}, USER={username}, PASSWORD={password}, PORT={port}")

# Banco de teste temporário
temp_database = "teste_temp"

try:
    # Conexão inicial com o banco padrão
    conn = psycopg2.connect(
        host=server,
        user=username,
        password=password,
        port=port,
        dbname=database
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Criação do banco temporário, se não existir
    cursor.execute(
        sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [temp_database]
    )
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(temp_database)))
        # print(f"✅ Banco '{temp_database}' criado com sucesso!")

    # Conectar ao banco criado
    cursor.close()
    conn.close()
    conn = psycopg2.connect(
        host=server,
        user=username,
        password=password,
        port=port,
        dbname=temp_database
    )
    cursor = conn.cursor()

    # Cria uma tabela exemplo
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100),
            email VARCHAR(100)
        );
    """)
    conn.commit()
    print("✅ Conexão estabelecida com o PostgreSQL!")

    # (Opcional) Remover o banco de teste
    cursor.close()
    conn.close()

    conn = psycopg2.connect(
        host=server,
        user=username,
        password=password,
        port=port,
        dbname="postgres"
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.SQL("DROP DATABASE IF EXISTS {}").format(sql.Identifier(temp_database)))
    # print("🗑️ Banco temporário removido com sucesso!")

    cursor.close()
    conn.close()

except Exception as e:
    print("❌ Falha de conexão com o PostgreSQL!")
    # print("Erro:", e)

