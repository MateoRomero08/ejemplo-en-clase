import pandas as pd

def extract_csv(path: str) -> pd.DataFrame:
    """
    EXTRAER datos desde un archivo CSV.
    - path: ruta al archivo CSV (ej. data/raw/dataset.csv)
    - return: DataFrame de Pandas con los datos cargados
    """
    df = pd.read_csv(path)
    return df
