# 3. Descriptive Statistics
# The following code shows some dataframes which give us some fast information about the dataset.
import pandas as pd


# Ruta donde se obtendrá el archivo CSV
route = 'C:/Users/Miguel Sanka/Desktop/crimen_nac_clean.csv'

# Ruta donde se guardarán los archivos CSV
months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

#Se lee el csv en un dataframe
df_crime = pd.read_csv(route, encoding='latin')

# Df con filas de estados y columnas de meses
def total_per_state(year: int) -> pd.DataFrame:
    filtered_df = df_crime[df_crime['Año'] == year]
    return filtered_df.groupby('Entidad')[months].sum()

# df con fila de año y columnas de meses
def total_per_year(year: int) -> pd.DataFrame:
    filtered_df = df_crime[df_crime['Año'] == year]
    return filtered_df.groupby('Año')[months].sum()

# df con filas de años y columnas de meses
def total_per_syear() -> pd.DataFrame:
    return df_crime.groupby('Año')[months].sum()

# df con meses y sumatoria de crimenes
def total_per_month(year: int) -> pd.DataFrame:
 df_filtered = df_crime[df_crime['Año'] == year]
 return df_filtered.groupby('Entidad')[months].sum().sum()

# df con filas de subcrimenes y columnas de años
def total_subcrime(year: int) -> pd.DataFrame:
   df_filtered = df_crime[df_crime['Año'] == year]
   return df_filtered.groupby('Subtipo de delito')[months].sum()

# df con filas de crimenes y columnas de años
def total_crime(year: int) -> pd.DataFrame:
   df_filtered = df_crime[df_crime['Año'] == year]
   return df_filtered.groupby('Tipo de delito')[months].sum()


# Ejecución de las funciones
# print(total_crime(2020))

print(total_subcrime(2020))
print("\n")

print(total_per_state(2020))
print("\n")

print(total_per_year(2020))
print("\n")

df_total_per_syear = total_per_syear()
print(df_total_per_syear)
df_total_per_syear.to_csv('C:/Users/Miguel Sanka/Desktop/crimen_total_per_year.csv', encoding='latin')
print("\n")

df_total_per_month = total_per_month(2020)
print(df_total_per_month)
df_total_per_syear.to_csv('C:/Users/Miguel Sanka/Desktop/crimen_total_per_month.csv', encoding='latin')
print("\n")
