import polars as pl

def get_data() -> pl.DataFrame :


    uri = "postgresql://postgres:HelloWorld4000!@db.jzrnhsvugvjfkchkucuv.supabase.co:5432/postgres"
    query = "SELECT * FROM mtpl_db"

    df = pl.read_database_uri(query=query, uri=uri, engine = "adbc")

    return df
