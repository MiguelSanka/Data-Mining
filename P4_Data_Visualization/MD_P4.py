# Practice 4: Data Visualization
# Miguel Ángel Sánchez Carrillo 
# ID: 1912006 Group: 036

import plotly.express as px
import numpy as np
import pandas as pd

# Ruta donde se obtendrá el archivo CSV
route = 'C:/Users/Miguel Sanka/Desktop/crimen_nac_clean.csv'
months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

#Se lee el csv en un dataframe
df_crime = pd.read_csv(route, encoding='latin')

#Funciones que retornan dataframe para utilizar en las gráficas
def total_per_year(year: int) -> pd.DataFrame:
    filtered_df = df_crime[df_crime['Año'] == year]
    return filtered_df.groupby('Año')[months].sum().transpose()

def total_per_syear() -> pd.DataFrame:
    return df_crime.groupby('Año')[months].sum()

def total_per_state(year: int) -> pd.DataFrame:
    filtered_df = df_crime[df_crime['Año'] == year]
    return filtered_df.groupby('Entidad')[months].sum()

def total_crime(year: int) -> pd.DataFrame:
   df_filtered = df_crime[df_crime['Año'] == year]
   return df_filtered.groupby('Tipo de delito')[months].sum()


# Función para generar un gráfico de barras de los crimenes por mes de un año específico
def generate_bars_crime_month(year: int) -> None: 
    df = total_crime(year)#Crimenes por mes
    fig = px.bar(df, x=months, title="Crimenes por tipo {}".format(year))
    fig.update_layout(bargap=0.2)
    fig.update_layout(
        font_family="Courier New",
        title_font_family="Times New Roman",
        title_font_color="blue",
        title_font_size=40,
        legend_title_font_color="green"
    )
    fig.show()
    fig.write_html("C:/Users/Miguel Sanka/Desktop/" + "Crimenes por tipo {}".format(year) + ".html")

# Función para generar un gráfico de barras de los crimenes por estado de un año específico
def generate_bars_crime_state(year: int)-> None: 
    df = total_per_state(2022) #Crimenes por estado
    fig = px.bar(df, x=months, title="Crimenes por entidad {}".format(year))
    fig.update_layout(
        font_family="Courier New",
        title_font_family="Times New Roman",
        template='plotly_dark',
        title_font_color="white",
        title_font_size=40,
    )
    fig.show()
    fig.write_html("C:/Users/Miguel Sanka/Desktop/" + "Crimenes por entidad {}".format(year) + ".html")

# F. para generar un gráficos de pastel de los delitos de todas las entidades de un año especifico
def generate_pie_mexico(year: int) -> None: 
    df = df_crime.query("Año == {}".format(year))
    
    for _ in range(12):
        fig = px.pie(df, values=months[_], names='Tipo de delito', title='Delitos en {} de {} México'.format(months[_], year))
        fig.show()
        fig.write_html("C:/Users/Miguel Sanka/Desktop/" + 'Delitos en {} de {} México'.format(months[_], year) + ".html")

# F. para generar gráficos de pastel de los delitos de una entidad y un año especifico
def generate_pie_state(year: int, state: str) -> None: 
    df = df_crime.query("Año == {}".format(year)).query("Entidad == '{}'".format(state))
    
    for _ in range(12):
        fig = px.pie(df, values=months[_], names='Tipo de delito', title='Delitos en {} de {} {}'.format(months[_], year, state))
        fig.show()
        fig.write_html("C:/Users/Miguel Sanka/Desktop/" + 'Delitos en {} de {} {}'.format(months[_], year, state) + ".html")


# Caja de bigote de los crimes del 2022
df_2022 = total_per_state(2022)
fig = px.box(df_2022, title="Caja de bigote de crimenes por mes 2022")
fig.show()
#fig.write_html("C:/Users/Miguel Sanka/Desktop/Caja de bigote de crimenes por mes 2022.html")


# Generación de gráficas utilizando las funciones anteriormente definidas.
#generate_bars_crime_state(2022)
#generate_bars_crime_month(2022)
#generate_pie_state(2022, "Nuevo León")
#generate_pie_mexico(2022)

