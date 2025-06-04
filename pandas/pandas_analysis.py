"""
pandas_analysis.py
------------------
Demuestra:
- Carga de datos
- Limpieza (dropna, renombrar columnas si fuera necesario)
- Filtrado y subsetting
- Agregaciones con groupby
- Operaciones de series temporales
"""

import pandas as pd
from utils.loader import load_data

def analyze_pandas():
    # 1) Cargar datos
    df = load_data()

    # 2) Limpieza básica (ejemplo)
    df = df.dropna()
    # (Si quisieras renombrar columnas, ejemplar: df.rename(columns={'Old':'New'}, inplace=True))

    print("\n[INFO] Primeras filas del DataFrame limpio:")
    print(df.head())

    # 3) Filtrado: ventas mayores a 1000 de ingresos totales
    high_revenue = df[df['Total_Revenue'] > 1000]
    print(f"\n[INFO] Registros con Total_Revenue > 1000: {len(high_revenue)}")

    # 4) GroupBy: sumar ingresos y contar unidades por región
    grouped_region = df.groupby('Region').agg(
        Total_Revenue_Region=('Total_Revenue', 'sum'),
        Total_Units=('Units_Sold', 'sum'),
        Transactions=('Date', 'count')
    ).reset_index()
    print("\n[INFO] Agrupado por Región:")
    print(grouped_region)

    # 5) Operaciones de series temporales: ingresos totales mensuales
    df_ts = df.set_index('Date').sort_index()
    monthly_revenue = df_ts['Total_Revenue'].resample('M').sum().reset_index()
    print("\n[INFO] Total de ingresos por mes:")
    print(monthly_revenue)

    # 6) Exportar resultados (opcional)
    monthly_revenue.to_csv('../data/monthly_revenue.csv', index=False)
    print("\n[INFO] monthly_revenue.csv generado en carpeta data/")

if __name__ == "__main__":
    analyze_pandas()
