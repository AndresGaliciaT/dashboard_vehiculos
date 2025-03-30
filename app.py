import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el dataset (si ya lo tienes en tu repositorio)
car_data = pd.read_csv('vehicles_us.csv')

# Título de la app
st.header('Panel de Control de Ventas de Coches')

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creando un histograma...')
    fig = px.histogram(car_data, x="odometer")  # Cambia el nombre de la columna según tu dataset
    st.plotly_chart(fig)