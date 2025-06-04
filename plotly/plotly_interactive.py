"""
plotly_interactive.py
---------------------
Demuestra:
- Gráfico de línea interactivo con slider
- Gráfico de barras interactivo con dropdown
"""

import os, sys

# --- Agrego la carpeta padre al path para que 'utils/' sea visible ---
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.loader import load_data

def plotly_demo():
    df = load_data()

    # 1) Gráfico de línea interactivo: Ingreso mensual
    df_ts = df.set_index('Date').sort_index()
    monthly_revenue = df_ts['Total_Revenue'].resample('ME').sum().reset_index()

    fig_line = px.line(
        monthly_revenue,
        x='Date',
        y='Total_Revenue',
        title='Ingreso Mensual Interactivo',
        labels={'Total_Revenue': 'Total Revenue', 'Date': 'Fecha'},
        markers=True
    )
    fig_line.update_layout(
        xaxis=dict(rangeslider=dict(visible=True)),
        hovermode='x unified'
    )
    fig_line.write_html('interactive_line_revenue.html', auto_open=False)
    print("[INFO] interactive_line_revenue.html generado")

    # 2) Gráfico de barras interactivo: Unidades vendidas por categoría para cada año
    df['Year'] = df['Date'].dt.year.astype(str)
    years = df['Year'].unique().tolist()

    fig_bar = go.Figure()
    for yr in years:
        df_yr = df[df['Year'] == yr]
        category_year = df_yr.groupby('Category')['Units_Sold'].sum().reset_index()
        fig_bar.add_trace(
            go.Bar(
                x=category_year['Category'],
                y=category_year['Units_Sold'],
                name=f'Año {yr}',
                visible=(yr == years[0])
            )
        )

    buttons = []
    for i, yr in enumerate(years):
        visibility = [j == i for j in range(len(years))]
        buttons.append(
            dict(
                label=f'{yr}',
                method='update',
                args=[{'visible': visibility},
                      {'title': f'Unidades Vendidas por Categoría ({yr})'}]
            )
        )

    fig_bar.update_layout(
        updatemenus=[dict(active=0, buttons=buttons, x=1.1, y=1.15)],
        title=f'Unidades Vendidas por Categoría ({years[0]})',
        xaxis_title='Categoría',
        yaxis_title='Units Sold'
    )

    fig_bar.write_html('interactive_bar_category.html', auto_open=False)
    print("[INFO] interactive_bar_category.html generado")

if __name__ == "__main__":
    plotly_demo()
