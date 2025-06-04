"""
seaborn_visuals.py
------------------
Demuestra:
- Histogramas con KDE
- Boxplots por categoría
- Heatmap de correlación
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils.loader import load_data

def seaborn_demo():
    df = load_data()

    # 1) Histograma y KDE de Total_Revenue
    plt.figure(figsize=(6, 4))
    sns.histplot(df['Total_Revenue'], kde=True)
    plt.title('Distribución de Total Revenue')
    plt.xlabel('Total Revenue')
    plt.tight_layout()
    plt.savefig('histogram_revenue.png')
    plt.close()
    print("[INFO] histogram_revenue.png generado")

    # 2) Boxplot: Total_Revenue por Región
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='Region', y='Total_Revenue', data=df)
    plt.title('Boxplot de Total Revenue por Región')
    plt.tight_layout()
    plt.savefig('boxplot_revenue_region.png')
    plt.close()
    print("[INFO] boxplot_revenue_region.png generado")

    # 3) Heatmap de correlación numérica
    numeric_cols = df.select_dtypes(include='number')
    corr = numeric_cols.corr()
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Matriz de Correlación')
    plt.tight_layout()
    plt.savefig('heatmap_correlation.png')
    plt.close()
    print("[INFO] heatmap_correlation.png generado")

if __name__ == "__main__":
    seaborn_demo()
