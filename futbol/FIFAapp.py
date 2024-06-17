import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from io import BytesIO
import requests
from streamlit_autorefresh import st_autorefresh

# Refrescar la página cada 30 segundos
count = st_autorefresh(interval=30 * 1000, key="dashboard_refresh")

# Selección de pestaña
page = st.selectbox("Selecciona una pestaña", ["Portada", "Dashboard"])

# Pestaña de Portada
if page == "Portada":
    col1, col2 = st.columns(2)

    with col1:
        url = "https://static.wikia.nocookie.net/revenge-history/images/6/62/Fifa-logo.jpg/revision/latest?cb=20181028155036&path-prefix=es"
        response = requests.get(url)
        
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.image(image, caption='Logo de la FIFA', use_column_width=True)
        else:
            st.error("No se pudo descargar la imagen. Código de estado: " + str(response.status_code))

    with col2:
        st.header('Descripción del Dataset')
        st.write('''Este conjunto de datos incluye 47,126 resultados de partidos internacionales de fútbol desde el primer partido oficial en 1872 hasta 2024. 
        Los partidos varían desde la Copa Mundial de la FIFA hasta la Copa Salvaje FIFI y partidos amistosos regulares. 
        Los partidos son estrictamente internacionales completos de hombres y los datos no incluyen Juegos Olímpicos o partidos donde al menos uno de los equipos fue el equipo B de la nación, sub-23 o un equipo selecto de la liga.''')

        st.write('**results.csv** incluye las siguientes columnas:')
        st.write('''
        - date: fecha del partido
        - home_team: nombre del equipo local
        - away_team: nombre del equipo visitante
        - home_score: puntuación del equipo local al final del tiempo reglamentario, incluyendo tiempo extra, no incluye tandas de penales
        - away_score: puntuación del equipo visitante al final del tiempo reglamentario, incluyendo tiempo extra, no incluye tandas de penales
        - tournament: nombre del torneo
        - city: nombre de la ciudad/pueblo/unidad administrativa donde se jugó el partido
        - country: nombre del país donde se jugó el partido
        - neutral: columna TRUE/FALSE que indica si el partido se jugó en un terreno neutral
        ''')

        st.write('**shootouts.csv** incluye las siguientes columnas:')
        st.write('''
        - date: fecha del partido
        - home_team: nombre del equipo local
        - away_team: nombre del equipo visitante
        - winner: ganador de la tanda de penales
        - first_shooter: equipo que comenzó primero en la tanda de penales
        ''')

        st.write('**goalscorers.csv** incluye las siguientes columnas:')
        st.write('''
        - date: fecha del partido
        - home_team: nombre del equipo local
        - away_team: nombre del equipo visitante
        - team: nombre del equipo que anotó el gol
        - scorer: nombre del jugador que anotó el gol
        - own_goal: si el gol fue en propia puerta
        - penalty: si el gol fue un penal
        ''')

        st.write('Nota sobre los nombres de equipos y países: Para los equipos locales y visitantes se ha utilizado el nombre actual del equipo. Por ejemplo, cuando en 1882 un equipo que se llamaba Irlanda jugó contra Inglaterra, en este conjunto de datos, se llama Irlanda del Norte porque el equipo actual de Irlanda del Norte es el sucesor del equipo de Irlanda de 1882. Esto se hace para que sea más fácil rastrear la historia y las estadísticas de los equipos.')

        st.write('Para los nombres de los países, se utiliza el nombre del país en el momento del partido. Así que cuando Ghana jugó en Accra, Gold Coast en la década de 1950, aunque los nombres del equipo local y el país no coincidan, fue un partido en casa para Ghana. Esto se indica en la columna neutral, que dice FALSE para esos partidos, lo que significa que no fue en un terreno neutral.')

# Pestaña de Dashboard
elif page == "Dashboard":
    # Cargar los datos
    results = pd.read_csv('results.csv')
    results['date'] = pd.to_datetime(results['date'])

    # Filtros de tiempo
    start_year, end_year = st.slider(
        'Selecciona el rango de años',
        min_value=int(results['date'].dt.year.min()),
        max_value=int(results['date'].dt.year.max()),
        value=(int(results['date'].dt.year.min()), int(results['date'].dt.year.max()))
    )

    # Filtrar los datos según el rango de tiempo seleccionado
    filtered_data = results[(results['date'].dt.year >= start_year) & (results['date'].dt.year <= end_year)]

    # Crear las visualizaciones
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        home_wins = filtered_data[filtered_data['home_score'] > filtered_data['away_score']].shape[0]
        st.metric(label="Partidos Ganados de Local", value=home_wins)

    with col2:
        away_wins = filtered_data[filtered_data['away_score'] > filtered_data['home_score']].shape[0]
        st.metric(label="Partidos Ganados de Visitante", value=away_wins)

    with col3:
        goals_scored = filtered_data['home_score'].sum() + filtered_data['away_score'].sum()
        st.metric(label="Goles Anotados", value=goals_scored)

    with col4:
        num_matches = filtered_data.shape[0]
        st.metric(label="Número de Partidos", value=num_matches)

    # Gráficos adicionales
    st.subheader("Análisis de Partidos")

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(data=filtered_data, x='date', y='home_score', label='Goles Local', ax=ax)
    sns.lineplot(data=filtered_data, x='date', y='away_score', label='Goles Visitante', ax=ax)
    ax.set_title('Goles por Año')
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 4))
    match_counts = filtered_data.groupby(filtered_data['date'].dt.year).size()
    match_counts.plot(kind='bar', ax=ax)
    ax.set_title('Número de Partidos por Año')
    st.pyplot(fig)
