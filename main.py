from extract.extract_data import extract_csv
from load.load_data import load_to_sqlite
from transform.transform_data import transform

if __name__ == "__main__":
    # Paso 1: Extraer CSV
    df = extract_csv("data/raw/dataset.csv")

    # Paso 2: Cargar datos crudos en base SQLite
    load_to_sqlite(df)

    # Paso 3: Transformar datos (limpieza)
    clean_df = transform()

    # Mostrar resultado
    print("✅ Proceso ELT completado. Datos limpios:")
    print(clean_df.head())
