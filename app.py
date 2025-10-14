import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Título de la app
st.title("Análisis de Consumo Energético en Producción de Acero")

# Cargar datos
data_path = "data/acero.csv"
df = pd.read_csv(data_path)
# Limpiar y convertir la columna 'consumo' a numérica
df['consumo'] = df['consumo'].astype(str).str.replace(',', '.', regex=False).str.replace('"', '', regex=False)
df['consumo'] = pd.to_numeric(df['consumo'], errors='coerce')

st.header("Estadísticas Descriptivas")
st.write(df.describe())

# Visualización: Consumo por línea de producción
st.header("Consumo Energético por Línea de Producción")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="linea", y="consumo", data=df, ax=ax)
ax.set_xlabel("Línea de Producción")
ax.set_ylabel("Consumo Energético")

st.pyplot(fig)

# Boxplot comparativo entre líneas A, B y C
st.header("Comparación de Consumo: Líneas A, B y C")
df_abc = df[df['linea'].isin(['A', 'B', 'C'])]
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.boxplot(x="linea", y="consumo", data=df_abc, ax=ax2, palette="Set2")
ax2.set_title("Consumo Energético por Línea (A, B, C)")
ax2.set_xlabel("Línea de Producción")
ax2.set_ylabel("Consumo Energético")
st.pyplot(fig2)

# ANOVA de un factor
st.header("Análisis ANOVA de un Factor")

model = ols('consumo ~ C(linea)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Mostrar tabla ANOVA
st.subheader("Tabla de Resultados ANOVA")
st.dataframe(anova_table)

# Interpretación automática del valor p
p_value = anova_table['PR(>F)'][0]
st.subheader("Interpretación del valor p")
if p_value < 0.05:
    st.success(f"El valor p es {p_value:.4f}. Esto significa que hay evidencia suficiente para afirmar que existen diferencias significativas en el consumo energético entre las líneas de producción. En otras palabras, al menos una línea consume energía de manera diferente a las demás.")
else:
    st.info(f"El valor p es {p_value:.4f}. Esto indica que no hay evidencia suficiente para afirmar que existen diferencias en el consumo energético entre las líneas de producción. Es decir, todas las líneas tienen consumos similares desde el punto de vista estadístico.")
