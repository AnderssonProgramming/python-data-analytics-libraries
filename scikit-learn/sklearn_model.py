"""
sklearn_model.py
----------------
Demuestra:
- División de datos en entrenamiento/prueba
- Entrenamiento de un modelo de regresión lineal
- Evaluación con MSE y R²
- Predicción de totales de ingreso en función de Units_Sold y Unit_Price
"""

import os, sys

# --- Agrego la carpeta padre al path para que 'utils/' sea visible ---
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from utils.loader import load_data

def sklearn_demo():
    df = load_data()

    # 1) Variables predictoras y objetivo
    X = df[['Units_Sold', 'Unit_Price']]
    y = df['Total_Revenue']

    # 2) División train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # 3) Entrenar regresión lineal
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    # 4) Predicción y evaluación
    y_pred = lr.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\n[RESULT] MSE: {mse:.2f}")
    print(f"[RESULT] R²: {r2:.2f}")

    # 5) Gráfico: Actual vs Predicho
    plt.figure(figsize=(6, 4))
    plt.scatter(y_test, y_pred, alpha=0.7, edgecolors='w')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
             'r--', lw=2, label='Ideal Fit')
    plt.xlabel('Actual Total Revenue')
    plt.ylabel('Predicted Total Revenue')
    plt.title('Regresión Lineal: Actual vs Predicho')
    plt.legend()
    plt.tight_layout()
    plt.savefig('linear_regression_revenue.png')
    plt.close()
    print("[INFO] linear_regression_revenue.png generado")

if __name__ == "__main__":
    sklearn_demo()
