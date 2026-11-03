import polars as pl
from dotenv import load_dotenv
import os

def get_data() -> pl.DataFrame :

    load_dotenv()
    pwd = os.getenv('PASS')
    usr = os.getenv('USERNAME')
    srv = os.getenv('SRV')
    host = os.getenv('HOST')
    uri = f"postgresql://{usr}:{pwd}@{srv}:{host}/postgres"
    query = "SELECT * FROM mtpl_db"

    df = pl.read_database_uri(query=query, uri=uri, engine = "adbc")

    return df


