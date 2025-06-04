# 🐍 Python Data Analytics Libraries

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-brightgreen.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Latest-orange.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Latest-red.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Latest-blue.svg)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Latest-9cf.svg)](https://plotly.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-yellow.svg)](https://scikit-learn.org/)

</div>

## 📋 Overview
This repository serves as a practical guide to the most powerful Python libraries for data analysis and visualization. It provides clear, executable examples of how to perform common data tasks, from basic data manipulation to statistical analysis and machine learning. Each module demonstrates real-world workflows that data scientists and analysts use every day.

### 📊 Dataset Description
All examples work with the same `sample_dataset.csv` which contains retail sales data with the following columns:
- **Date**: Transaction date
- **Region**: Sales region (North, South, East, West)
- **Category**: Product category (Clothing, Electronics, Home & Kitchen)
- **Units_Sold**: Number of units sold
- **Unit_Price**: Price per unit
- **Total_Revenue**: Total revenue from transaction
- **Avg_Customer_Age**: Average age of customers
- **Customer_Rating**: Customer satisfaction rating (1-5)

### 🚀 Structure

```plaintext
python-data-analytics-libraries/
│
├── data/
│   └── sample_dataset.csv
│
├── utils/
│   └── loader.py
│
├── pandas/
│   └── pandas_analysis.py
│
├── numpy/
│   └── numpy_operations.py
│
├── matplotlib/
│   └── matplotlib_visuals.py
│
├── seaborn/
│   └── seaborn_visuals.py
│
├── plotly/
│   └── plotly_interactive.py
│
├── scikit-learn/
│   └── sklearn_model.py
│
├── README.md
└── requirements.txt
```


### 📊 How to Run Each Module

1. Clone the repository:

```bash
git clone https://github.com/AnderssonProgramming/python-data-analytics-libraries.git
cd python-data-analytics-libraries
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. For each module, navigate to its folder and execute:

```bash
# Pandas - Tabular analysis and data manipulation
cd pandas
python pandas_analysis.py

# NumPy - Numerical and mathematical operations
cd ../numpy
python numpy_operations.py

# Matplotlib - Static visualizations
cd ../matplotlib
python matplotlib_visuals.py

# Seaborn - Advanced statistical visualizations
cd ../seaborn
python seaborn_visuals.py

# Plotly - Interactive charts
cd ../plotly
python plotly_interactive.py

# scikit-learn - Predictive modeling
cd ../scikit-learn
python sklearn_model.py
```

4. Inspect the generated files (CSVs, PNGs, HTMLs) in their respective directories.

### 📊 Generated Outputs

- **Pandas**: CSV files with transformed data and statistical summaries
- **NumPy**: Numerical transformations and matrix calculations
- **Matplotlib**: Static bar, line, and pie charts (.png)
- **Seaborn**: Advanced statistical visualizations like KDE histograms, boxplots, and heatmaps
- **Plotly**: Interactive HTML charts for data exploration
- **scikit-learn**: Predictive models and results visualization

### 🔍 Highlighted Examples

- **Pandas**: Data aggregation by region and time series analysis
- **Seaborn**: Correlation heatmaps between numerical variables
- **Plotly**: Interactive charts with hover and zoom capabilities
- **scikit-learn**: Regression models to predict revenue

---

<div align="center">
  
### 🛠 Technologies Used

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" alt="numpy" width="40" height="40"/>
<img src="https://matplotlib.org/stable/_images/sphx_glr_logos2_003.png" alt="matplotlib" width="40" height="40"/>
<img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/>
<img src="https://images.crunchbase.com/image/upload/c_pad,f_auto,q_auto:eco,dpr_1/vgay5hqdvszlmvud3hwu" alt="plotly" width="40" height="40"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit-learn" width="40" height="40"/>

</div>

---
