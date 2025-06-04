"""
numpy_operations.py
-------------------
Demuestra:
- Carga de datos en pandas y conversión a NumPy
- Estadísticas básicas
- Normalización de columnas numéricas
- Operaciones vectorizadas
"""

import os, sys

# --- Agrego la carpeta padre al path para que 'utils/' sea visible ---
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import pandas as pd
from utils.loader import load_data

def numpy_demo():
    # 1) Cargar datos y seleccionar columnas numéricas
    df = load_data()
    numeric_cols = df[['Units_Sold', 'Unit_Price', 'Total_Revenue', 'Avg_Customer_Age', 'Customer_Rating']]
    arr = numeric_cols.to_numpy()

    print("\n[INFO] Array NumPy con datos numéricos (5 primeras filas):")
    print(arr[:5, :])

    # 2) Estadísticas básicas con NumPy
    print("\n[INFO] Media por columna:", np.mean(arr, axis=0))
    print("[INFO] Mediana por columna:", np.median(arr, axis=0))
    print("[INFO] Desviación estándar:", np.std(arr, axis=0))

    # 3) Normalización (Min-Max) de cada columna
    min_vals = arr.min(axis=0)
    max_vals = arr.max(axis=0)
    normalized = (arr - min_vals) / (max_vals - min_vals)
    print("\n[INFO] Datos normalizados (5 primeras filas):")
    print(normalized[:5, :])

    # 4) Operaciones vectorizadas de muestra
    # Ejemplo: calcular ganancias = Total_Revenue - (Units_Sold * costo_estimado)
    costo_estimado = np.array([unit_price_map] if False else np.zeros(arr.shape[1]))  # placeholder si quisieras restar costos
    # Aquí sólo mostramos un ejemplo simple de raíz cuadrada de las ventas
    sqrt_units = np.sqrt(arr[:, 0])
    print("\n[INFO] Raíz cuadrada de Units_Sold (primeros 5):", sqrt_units[:5])

if __name__ == "__main__":
    numpy_demo()
