# Practice 7: Data classification

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

route = 'C:/Users/Miguel Sanka/Desktop/crimen_nac_clean.csv'
months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
df_crime = pd.read_csv(route, encoding='latin')

# Función para obtener el total de crimenes por mes de un año específico
def sum_per_month(year: int, state: str) -> pd.DataFrame:
    df_year = df_crime.query("Año == {} & Entidad == '{}'".format(year, state))[months].sum()
    df_year = pd.DataFrame({'Month number': range(1, 13), 'Crimes':df_year.values}, index=df_year.index)
    df_year.index.name = "Month"
    return df_year

# Función para generar la clasificación del número de crimenes de un estado y año específicos
def gen_KNeighborsClassifier(year: int, state: str) -> None:
    df_20XX = sum_per_month(year, state)
    avg_crimes = df_20XX['Crimes'].mean()
    std = df_20XX['Crimes'].std()
    intervals = [0, avg_crimes - std/3, avg_crimes + std/3, np.inf]
    labels = ['Low', 'Normal', 'High']
    df_20XX['Class'] = pd.cut(df_20XX['Crimes'], bins=intervals, labels=labels, include_lowest=True)

    X = df_20XX[['Month number']]
    y = df_20XX['Crimes']
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y)

    X_pred = np.array(range(1, 13)).reshape(-1, 1)
    class_colors = {'Low': 'blue', 'Normal': 'purple', 'High': 'red'}

    plt.figure(figsize=(15, 9))

    # Añadir los colores a las etiquetas
    for class_label, color in class_colors.items():
        plt.scatter(
            df_20XX['Month number'][df_20XX['Class'] == class_label],
            df_20XX['Crimes'][df_20XX['Class'] == class_label],
            c=color,
            label=f'{class_label}'
        )
    plt.scatter(df_20XX['Month number'], df_20XX['Crimes'], c=df_20XX['Class'].map(class_colors))
    plt.scatter(X_pred, knn.predict(X_pred), c='green', marker='x', s=100, label='Predictions')
    plt.axhline(y=avg_crimes, color='k', linestyle='--', label=f'Average ({avg_crimes:.2f})')
    plt.xlabel('Month number')
    plt.ylabel('Crimes')
    plt.legend()
    plt.title("KNeighborsClassifier crimes {} {}".format(state, year))
    plt.xticks(range(1,13))
    plt.savefig("C:/Users/Miguel Sanka/Desktop/KNeighborsClassifier {} {}.png".format(state, year))
    #plt.show()

for year in range(2015, 2023):
    gen_KNeighborsClassifier(year, "Nuevo León")
