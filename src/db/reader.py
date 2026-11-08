import polars as pl
from dotenv import load_dotenv
import os
import polars_redis as redis

@redis.cache(url="redis://localhost:6379", ttl=3600)
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


