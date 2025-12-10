# ============================================================
# IMPORTAR LIBRERÍAS
# ============================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


# ============================================================
# FUNCIÓN PARA GUARDAR FIGURAS
# ============================================================
contador = 1

def guardar(nombre):
    global contador
    archivo = f"{contador:02d}_{nombre}.png"
    plt.savefig(archivo, dpi=300, bbox_inches="tight")
    print(f"Guardado: {archivo}")
    contador += 1


# ============================================================
# CARGA DEL DATASET
# ============================================================
ruta = "superstore_dataset2012.csv"
df = pd.read_csv(ruta, encoding='latin1')

print("Primeras filas del dataset:")
print(df.head())

print("\nInformación del dataset:")
print(df.info())


# ============================================================
# PREPARACIÓN DE LOS DATOS
# ============================================================
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')

print("\nValores nulos por columna:")
print(df.isna().sum())

df = df.dropna()


# ============================================================
# VISUALIZACIÓN UNIVARIANTE - MATPLOTLIB
# ============================================================

plt.hist(df["Sales"], bins=30, color="skyblue", edgecolor="black")
plt.title("Distribución de Ventas (Sales)")
plt.xlabel("Sales")
plt.ylabel("Frecuencia")
guardar("histograma_sales_matplotlib")
plt.show()


# ============================================================
# VISUALIZACIÓN UNIVARIANTE - SEABORN
# ============================================================

sns.boxplot(x=df["Profit"], color="orange")
plt.title("Distribución del Profit")
plt.xlabel("Profit")
guardar("boxplot_profit_seaborn")
plt.show()


# ============================================================
# VISUALIZACIÓN BIVARIANTE - MATPLOTLIB
# ============================================================

plt.scatter(df["Sales"], df["Profit"], alpha=0.5)
plt.title("Relación entre Sales y Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
guardar("scatter_sales_profit_matplotlib")
plt.show()


# ============================================================
# VISUALIZACIÓN BIVARIANTE - SEABORN
# ============================================================

sns.regplot(x="Sales", y="Profit", data=df, scatter_kws={"alpha":0.4})
plt.title("Sales vs Profit (Regplot)")
plt.xlabel("Sales")
plt.ylabel("Profit")
guardar("regplot_sales_profit_seaborn")
plt.show()


# ============================================================
# VISUALIZACIÓN MULTIVARIANTE - HEATMAP
# ============================================================

sns.heatmap(
    df[["Sales", "Quantity", "Profit", "Discount"]].corr(),
    annot=True, cmap="coolwarm"
)
plt.title("Mapa de Calor de Correlación")
guardar("heatmap_correlacion_seaborn")
plt.show()


# ============================================================
# VISUALIZACIÓN MULTIVARIANTE - PAIRPLOT
# ============================================================

sns.pairplot(df[["Sales","Quantity","Profit","Discount"]])
plt.suptitle("Análisis Multivariante: Pairplot", y=1.02)
plt.savefig("pairplot_multivariante.png", dpi=300, bbox_inches="tight")
print("Guardado: pairplot_multivariante.png")
plt.show()


# ============================================================
# SUBPLOTS
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14,10))
fig.suptitle("Conjunto de Visualizaciones", fontsize=16)

axes[0,0].hist(df["Sales"], bins=20, color="skyblue", edgecolor="black")
axes[0,0].set_title("Histograma de Sales")

sns.boxplot(x=df["Profit"], ax=axes[0,1], color="orange")
axes[0,1].set_title("Boxplot de Profit")

axes[1,0].scatter(df["Sales"], df["Profit"], alpha=0.5)
axes[1,0].set_title("Sales vs Profit")

sns.heatmap(
    df[["Sales","Quantity","Profit","Discount"]].corr(),
    annot=True, cmap="coolwarm", ax=axes[1,1]
)
axes[1,1].set_title("Correlación")

plt.tight_layout()
plt.savefig("subplots_dashboard.png", dpi=300, bbox_inches="tight")
print("Guardado: subplots_dashboard.png")
plt.show()


# ============================================================
# HISTOGRAMA FINAL EXTRA (YA ESTABA EN TU CÓDIGO)
# ============================================================

sns.histplot(df["Sales"], bins=30, kde=True, color="purple")
plt.title("Histograma Guardado de Sales (Final)")
plt.xlabel("Sales")
plt.ylabel("Frecuencia")
guardar("histograma_sales_final_seaborn")
plt.show()


print("\n=== TODAS LAS FIGURAS HAN SIDO GUARDADAS ===")
