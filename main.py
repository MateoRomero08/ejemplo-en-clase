from extract.extract_data import extract_csv
from load.load_data import load_to_sqlite
from transform.transform_data import transform

if __name__ == "__main__":
    # Paso 1: Extraer CSV
    df = extract_csv("data/raw/dataset.csv")

    # Paso 2: Transformar datos (limpieza) 
    clean_df = transform()

    # Paso 3: Cargar datos limpios en base SQLite
    load_to_sqlite(clean_df)

    # Mostrar resultado
    print("Proceso ELT completado. Datos limpios:")
    print(clean_df)
