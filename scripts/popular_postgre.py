from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Carrega variáveis do arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path, override=True)

# Lê as variáveis do ambiente
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")

# Cria URL de conexão para PostgreSQL
conn_url = URL.create(
    drivername="postgresql",
    username=username,
    password=password,
    host=server,
    port=int(port),
    database=database
)

# Cria engine SQLAlchemy
engine = create_engine(conn_url)

# Caminho dos arquivos CSV
csv_paths = {
    "customers": "data/customers.csv",
    "geolocation": "data/geolocation.csv",
    "order_items": "data/order_items.csv",
    "order_payments": "data/order_payments.csv",
    "order_reviews": "data/order_reviews.csv",
    "orders": "data/orders.csv",
    "payment_type": "data/payment_type.csv",
    "product_category_name_translation": "data/product_category_name_translation.csv",
    "products": "data/products.csv",
    "sellers": "data/sellers.csv"
}

# Importação dos CSVs
for table_name, file_path in csv_paths.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, con=engine, index=False, if_exists="replace")
    print(f"✅ Tabela '{table_name}' importada com sucesso.")
