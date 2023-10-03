# Practice 5: Analysis of Variance (ANOVA)

import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd

# Ruta donde se obtendrá el archivo CSV
route = 'C:/Users/Miguel Sanka/Desktop/crimen_nac_clean.csv'
months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
mexican_states = [
    "Aguascalientes",
    "Baja California",
    "Baja California Sur",
    "Campeche",
    "Chiapas",
    "Chihuahua",
    "Coahuila de Zaragoza",
    "Colima",
    "Durango",
    "Guanajuato",
    "Guerrero",
    "Hidalgo",
    "Jalisco",
    "México",
    "Michoacán de Ocampo",
    "Morelos",
    "Nayarit",
    "Nuevo León",
    "Oaxaca",
    "Puebla",
    "Querétaro",
    "Quintana Roo",
    "San Luis Potosí",
    "Sinaloa",
    "Sonora",
    "Tabasco",
    "Tamaulipas",
    "Tlaxcala",
    "Veracruz de Ignacio de la Llave",
    "Yucatán",
    "Zacatecas"
]

#Se lee el csv en un dataframe
df_crime = pd.read_csv(route, encoding='latin')
df_2022 = df_crime.query("Año == 2022")


def anova_year(year: int) -> None:
    df_crime_year = df_crime.query("Año == {}".format(year))
    print(year)
    for _ in range(12):
        year_lm = ols('{}~ C(Entidad)'.format(months[_]), data=df_crime_year).fit()
        print("\n" + '*' + months[_])
        table = sm.stats.anova_lm(year_lm, typ=1) #Type 1 ANOVA DataFrame
        print(table)


#anova_year(2023) The dataset does not contain information for some months of the current year.
anova_year(2022)