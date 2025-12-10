# 📈 Superstore Data Visualization Dashboard

This project generates a comprehensive set of visualizations using the **Superstore 2012** dataset and the libraries **Matplotlib** and **Seaborn**.

All figures are automatically saved as PNG files.

---

## 📊 Visualizations Included

### ✔ Univariate (Matplotlib)
- Histogram (Sales)

### ✔ Univariate (Seaborn)
- Boxplot (Profit)

### ✔ Bivariate (Matplotlib)
- Scatter plot (Sales vs Profit)

### ✔ Bivariate (Seaborn)
- Regplot (Sales vs Profit)

### ✔ Multivariate
- Correlation Heatmap  
- Pairplot  

### ✔ Dashboard (Subplots)
A 2×2 grid combining:
- Histogram  
- Boxplot  
- Scatter plot  
- Heatmap  

All exported automatically.

---

## 📦 Files
- `Dashboards.py`
- `superstore_dataset2012.csv`
- Saved figures in the root folder


## ▶️ Requirements and run the Program
```bash
pip install pandas numpy matplotlib seaborn
python Dashboards.py
