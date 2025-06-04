"""
matplotlib_visuals.py
---------------------
Demuestra:
- Gráficos de línea, barras, pastel
- Personalización de etiquetas, títulos y leyendas
- Guardar figuras como PNG
"""

import matplotlib.pyplot as plt
import pandas as pd
from utils.loader import load_data

def matplotlib_demo():
    df = load_data()

    # 1) Gráfico de línea: Total_Revenue a lo largo del tiempo
    df_ts = df.set_index('Date').sort_index()
    monthly_revenue = df_ts['Total_Revenue'].resample('M').sum()
    plt.figure(figsize=(8, 4))
    plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o', linestyle='-')
    plt.title('Ingreso Mensual Total')
    plt.xlabel('Fecha')
    plt.ylabel('Total Revenue')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('line_plot_revenue.png')
    plt.close()
    print("[INFO] line_plot_revenue.png generado")

    # 2) Gráfico de barras: Unidades vendidas por categoría
    category_units = df.groupby('Category')['Units_Sold'].sum()
    plt.figure(figsize=(6, 4))
    plt.bar(category_units.index, category_units.values)
    plt.title('Unidades Vendidas por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Units_Sold')
    plt.tight_layout()
    plt.savefig('bar_units_category.png')
    plt.close()
    print("[INFO] bar_units_category.png generado")

    # 3) Gráfico de pastel: Distribución de ventas por región (por recuento de transacciones)
    region_counts = df['Region'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(region_counts.values, labels=region_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Transacciones por Región')
    plt.tight_layout()
    plt.savefig('pie_transactions_region.png')
    plt.close()
    print("[INFO] pie_transactions_region.png generado")

if __name__ == "__main__":
    matplotlib_demo()
