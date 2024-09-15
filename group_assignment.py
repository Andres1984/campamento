import streamlit as st
import random
import time

# Dictionary containing names and their pre-assigned groups (sorted alphabetically)
name_to_group = {
    "ALBA TOBIAS, NATALI": 1,
    "ARBOLEDA SIERRA, JHONATAN MAURICIO": 2,
    "BEDOYA MUÑOZ, JHON DAVID": 5,
    "BELTRAN ALZATE, NICOLAS HERNANDO": 2,
    "CALPA FORERO, JHONNY ANDRES": 4,
    "CAMACHO GUTIERREZ, DANIEL SANTIAGO": 5,
    "CARDENAS CALDAS, NASSIR SANTIAGO": 3,
    "CASTRO GÓMEZ, SALOMÉ": 5,
    "CASTRO TORRES, SERGIO DAVID": 7,
    "DELGADO CASTRO, JUAN PABLO": 7,
    "DIAZ SUAREZ, TANIA MICHELL": 3,
    "DUARTE AREVALO, EMILY DAYANA": 3,
    "DUARTE AREVALO, EMILY DAYANA": 5,
    "ESPITIA LEIVA, JUAN ESTEBAN": 6,
    "FIGUEROA VILLADA, JESUS ARTURO": 1,
    "GARZON TERAN, SHARIK": 7,
    "GONZALEZ CASTAÑEDA, NATHALIA": 6,
    "GUTIERREZ CASTRO, BLEIKSTON HERNAN": 6,
    "GUAYAMBUCO ZABALA, CARLOS EDUARDO": 1,
    "HERRERA VILLALBA, BRAYAN ALEXANDER": 4,
    "HERNÁNDEZ NIETO, BRAYAN SEBASTIÁN": 4,
    "LOPEZ CELY, CESAR HUMBERTO": 3,
    "MERCHÁN BERNAL, JUAN ESTEBAN": 6,
    "MONROY HERRERA, SAMUEL FERNANDO": 7,
    "MUÑOZ GONZÁLEZ, JULIANA": 4,
    "OICATA CORREDOR, NICOLAS": 5,
    "QUIROGA TARQUINO, SEBASTIAN ALEJANDRO": 3,
    "REYES CASTELLANOS, JUAN DIEGO": 2,
    "SANTAMARIA ARCE, LAURENCE ALFREDO": 1,
    "SIERRA BARRETO, MARIA JOSE": 1,
    "TORO CHAPARRO, JHOAN SANTIAGO": 2,
    "VALBUENA PLAZAS, DANNA": 7,
    "VALLEJO VECIL, DANIEL HUMBERTO": 4,
    "ZAMBRANO CABALLERO, SEBASTIAN": 6
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

