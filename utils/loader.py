"""
loader.py
---------
Función reutilizable para cargar el CSV de datos.
"""

import pandas as pd

def load_data():
    """
    Carga el dataset contextual desde ../data/sample_dataset.csv
    Devuelve un DataFrame de pandas.
    """
    path = '../data/sample_dataset.csv'
    df = pd.read_csv(path, parse_dates=['Date'])
    return df

if __name__ == "__main__":
    df = load_data()
    print("[INFO] Data cargada con éxito. Primeras filas:\n", df.head())
