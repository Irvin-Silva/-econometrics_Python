# Importamoslaslibreríasrequeridas:
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-white")

data = pd.read_csv("C:/Users/irvin/Desktop/Econometría Python/Datasets/GujaratiPorter71.txt",
                   sep=" ", delimiter="\t")

data.head
data.shape  # Número de Filas y columnas
data.columns  # Nombres de las columnas
data.dtypes  # Tipos de datos
data.info()  # Resumen de la información
data.describe()  # Información de estadistica básica
data["FLR"].describe()  # Información de una variable concreta}
data[["CM", "PGNP", "FLR"]].describe()  # Información de un conjunto de variables
g = sns.pairplot(data, plot_kws={"color": "darkblue"},
                 diag_kws={"color": "darkblue"})
g.fig.suptitle("Relación entre paresde variables",
               fontsize=25,
               fontweight="bold")
plt.subplots_adjust(top=0.9)
g.fig.text(1, -.02,
           "Elaboración:",
           fontsize=13, fontweight="bold",
           ha="right")
g.fig.text(1, -.05,
           "",
           fontsize=12, ha="right")
plt.show()
