import sqlite3
import pandas as pd

def transform(db_name="data_lake.db", raw_table="raw_data", target_table="clean_data"):
    """
    TRANSFORMAR los datos cargados en la base:
    - Limpieza: eliminar nulos, duplicados
    - Estandarizar nombres de columnas a minúsculas
    - Guardar resultado en una nueva tabla 'clean_data'
    """
    conn = sqlite3.connect(db_name)

    # 1. Leer los datos crudos
    df = pd.read_sql(f"SELECT * FROM {raw_table}", conn)

    # 2. Eliminar duplicados y valores nulos
    df = df.dropna().drop_duplicates()

    # 3. Normalizar nombres de columnas
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # 4. Guardar datos transformados
    df.to_sql(target_table, conn, if_exists="replace", index=False)
    conn.close()

    return df
