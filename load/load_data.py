import sqlite3
import pandas as pd

def load_to_sqlite(df: pd.DataFrame, db_name="data_lake.db", table="clean_data"):
    """
    CARGAR los datos ya modificados y limpios a una base SQLite (data lake local).
    - df: DataFrame que contiene los datos extraídos
    - db_name: nombre de la base de datos (por defecto 'data_lake.db')
    - table: tabla destino donde se guardarán los datos limpios
    """
    conn = sqlite3.connect(db_name)
    df.to_sql(table, conn, if_exists="replace", index=False)
    conn.close()
