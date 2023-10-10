import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import shapiro

route = 'C:/Users/Miguel Sanka/Desktop/crimen_nac_clean.csv'
months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
df_crime = pd.read_csv(route, encoding='latin')

# Función para obtener el total de crimenes por mes de un año específico
def sum_per_month(year: int) -> pd.DataFrame:
    df_year = df_crime.query("Año == {}".format(year))[months].sum()
    df_year = pd.DataFrame({'Month number': range(1, 13), 'Crimes':df_year.values}, index=df_year.index)
    df_year.index.name = "Month"
    return df_year

df_20XX = sum_per_month(2021)

# Modelado de la regresión lineal
X = df_20XX['Month number']  # Número del mes
y = df_20XX['Crimes']   # Cantidad de crimenes durante el mes
X = sm.add_constant(X)  
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

plt.figure(figsize=(9, 6)) 
plt.scatter(X['Month number'], y, label='Real data', color='dodgerblue')  # Datos reales
plt.plot(X['Month number'], predictions, color='crimson', label='Linear Regression') 
plt.title("Crime per month Mexico")
plt.xlabel('Month number')
plt.ylabel('Crimes')
plt.legend()
plt.xticks(range(1,13))
plt.savefig("C:/Users/Miguel Sanka/Desktop/Linear Regression.png")

plt.show()

# Dataframe con la correlación entre las variables
df_corr = df_20XX.corr(method="pearson", numeric_only=True)
print("\n", df_corr,"\n")

# Errores
residuals = model.resid #Error, diferencia entre el valor real y el predicho
df_error = pd.DataFrame({'Residuals': residuals,
                          'Observed': df_20XX['Crimes'],
                          'Predicted': model.predict()})
print(df_error, "\n")

# Histograma de los errores
plt.figure(figsize=(10, 6)) 
plt.hist(df_error['Residuals'])
plt.title("Residuals of the LR")
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.savefig("C:/Users/Miguel Sanka/Desktop/Errors Histogram.png")
plt.show()


# Prueba de Shapiro–Wilk, para determinar si los errores siguien una distribución normal.
statistic, p_value = shapiro(df_error['Residuals'])
print("Estadístico de prueba (W):", statistic)
print("Valor p:", p_value)

alpha = 0.05  # Nivel de significancia
if p_value > alpha:
    print("Los errores parecen seguir una distribución normal (no se rechaza H0)")
else:
    print("Los errores no siguen una distribución normal (se rechaza H0)")