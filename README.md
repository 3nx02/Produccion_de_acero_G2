# Producción de Acero G2

Este proyecto analiza el consumo energético en distintas líneas de producción de una empresa de acero, utilizando el dataset `acero.csv`.

## Objetivos
- Comparar el consumo energético entre diferentes líneas de producción.
- Identificar si existen diferencias significativas mediante análisis estadístico ANOVA.
- Proporcionar visualizaciones y conclusiones basadas en los datos.

## Metodología
1. **Carga de datos:** Se utiliza el archivo `data/acero.csv` que contiene registros de consumo energético por línea de producción.
2. **Preprocesamiento:** Limpieza y organización de los datos para su análisis.
3. **Análisis ANOVA:** Aplicación de la prueba ANOVA para comparar el consumo energético entre las distintas líneas.
4. **Visualización:** Uso de herramientas como Streamlit y Plotly para mostrar resultados y gráficos interactivos.
5. **Conclusiones:** Interpretación de los resultados y recomendaciones.

## Referencias
- Archivo de datos: [`data/acero.csv`](data/acero.csv)
- Documentación de ANOVA: [Wikipedia - ANOVA](https://es.wikipedia.org/wiki/An%C3%A1lisis_de_la_varianza)

---


## Teoría: ANOVA (Análisis de la Varianza)
ANOVA es una técnica estadística que permite comparar las medias de tres o más grupos para determinar si existen diferencias significativas entre ellos. En este proyecto, se utiliza ANOVA de un factor para analizar si el consumo energético varía entre las distintas líneas de producción de acero.

El valor p obtenido en el ANOVA indica la probabilidad de que las diferencias observadas entre grupos sean debidas al azar:
- Si el valor p es menor a 0.05, se concluye que existen diferencias significativas entre las líneas de producción.
- Si el valor p es mayor o igual a 0.05, no hay evidencia suficiente para afirmar que existen diferencias.

## Interpretación de los Resultados
Al ejecutar el análisis ANOVA sobre el consumo energético:
- Si el resultado muestra un valor p < 0.05, significa que al menos una línea de producción consume energía de manera diferente a las demás. Esto puede deberse a factores operativos, tecnológicos o de gestión.
- Si el valor p ≥ 0.05, se interpreta que todas las líneas tienen consumos similares desde el punto de vista estadístico, y no hay diferencias relevantes entre ellas.

Estos resultados ayudan a la empresa a identificar oportunidades de mejora y optimización en el uso de energía, enfocando acciones en las líneas que presenten consumos atípicos.

---

Este proyecto utiliza Python y las siguientes librerías: streamlit, sympy, numpy, pandas, plotly, matplotlib, seaborn, statsmodels.