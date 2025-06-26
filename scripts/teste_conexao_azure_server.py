import os
from dotenv import load_dotenv
import pyodbc

# Carrega as variáveis do arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path, override=True)

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
driver = os.getenv("DB_DRIVER")

print(f"Variáveis carregadas: SERVER={server}, USER={username}, PASSWORD={password}, PORT={driver}")

connection_string = f"""
    DRIVER={{{driver}}};
    SERVER={server};
    DATABASE={database};
    UID={username};
    PWD={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
"""

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()
cursor.execute("SELECT TOP 5 * FROM sys.tables")
for row in cursor.fetchall():
    print(row)
