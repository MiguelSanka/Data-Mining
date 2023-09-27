import pandas as pd

# Ruta donde se obtendrá el archivo CSV
route = 'C:/Users/Miguel Sanka/Desktop/crimen_nac.csv'

# Ruta donde se guardará el nuevo archivo CSV
route_new_csv = route.replace('crimen_nac.csv', 'crimen_nac_clean.csv')

#Se lee el csv en un dataframe
df_crime = pd.read_csv(route, encoding='latin')

#Se rellenan los espacios vacios con ceros
df_crime.fillna(0, inplace=True)


#se guarda en la nueva ruta
df_crime.to_csv(route_new_csv, encoding='latin')