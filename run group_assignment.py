import streamlit as st
import random
import time

# Dictionary containing names and their pre-assigned groups
name_to_group = {
    "GUAYAMBUCO ZABALA, CARLOS EDUARDO": 1,
    "FIGUEROA VILLADA, JESUS ARTURO": 1,
    "SIERRA BARRETO, MARIA JOSE": 1,
    "SANTAMARIA ARCE, LAURENCE ALFREDO": 1,
    "ALBA TOBIAS, NATALI": 1,
    "ARBOLEDA SIERRA, JHONATAN MAURICIO": 2,
    "BELTRAN ALZATE, NICOLAS HERNANDO": 2,
    "REYES CASTELLANOS, JUAN DIEGO": 2,
    "TORO CHAPARRO, JHOAN SANTIAGO": 2,
    "CARDENAS CALDAS, NASSIR SANTIAGO": 3,
    "QUIROGA TARQUINO, SEBASTIAN ALEJANDRO": 3,
    "DIAZ SUAREZ, TANIA MICHELL": 3,
    "LOPEZ CELY, CESAR HUMBERTO": 3,
    "DUARTE AREVALO, EMILY DAYANA": 3,
    "HERRERA VILLALBA, BRAYAN ALEXANDER": 4,
    "CALPA FORERO, JHONNY ANDRES": 4,
    "MUÑOZ GONZÁLEZ, JULIANA": 4,
    "HERNÁNDEZ NIETO, BRAYAN SEBASTIÁN": 4,
    "VALLEJO VECIL, DANIEL HUMBERTO": 4,
    "BEDOYA MUÑOZ, JHON DAVID": 5,
    "CAMACHO GUTIERREZ, DANIEL SANTIAGO": 5,
    "CASTRO GÓMEZ, SALOMÉ": 5,
    "DUARTE AREVALO, EMILY DAYANA": 5,
    "OICATA CORREDOR, NICOLAS": 5,
    "GONZALEZ CASTAÑEDA, NATHALIA": 6,
    "ZAMBRANO CABALLERO, SEBASTIAN": 6,
    "MERCHÁN BERNAL, JUAN ESTEBAN": 6,
    "GUTIERREZ CASTRO, BLEIKSTON HERNAN": 6,
    "ESPITIA LEIVA, JUAN ESTEBAN": 6,
    "DELGADO CASTRO, JUAN PABLO": 7,
    "CASTRO TORRES, SERGIO DAVID": 7,
    "VALBUENA PLAZAS, DANNA": 7,
    "GARZON TERAN, SHARIK": 7,
    "MONROY HERRERA, SAMUEL FERNANDO": 7
}

# Streamlit app title
st.title("Group Number Spinner")

# Dropdown selection for name
name_input = st.selectbox("Select the name:", list(name_to_group.keys()))

# Button to start the spinning process
if st.button('Spin the Wheel'):
    if name_input:
        group = name_to_group.get(name_input)

        if group:
            st.write("Spinning to find your group...")

            # Simulate number spinning
            spin_placeholder = st.empty()
            for _ in range(30):  # Simulate 30 spins
                random_number = random.randint(1, 7)
                spin_placeholder.markdown(f"<h1 style='text-align: center;'>{random_number}</h1>", unsafe_allow_html=True)
                time.sleep(0.1)  # Control the speed of spinning

            # Display the final assigned group
            spin_placeholder.markdown(f"<h1 style='text-align: center; color: green;'>¡Felicidades! Tu grupo es: {group}</h1>", unsafe_allow_html=True)
