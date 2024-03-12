import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Detalle de vehiculos')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches') # escribir un mensaje
    fig = px.histogram(car_data, x="odometer") # crear un histograma
    st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo

disp_button = st.button('Construir grafico de dispersion') # crear un botón
        
if disp_button: # al hacer clic en el botón
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches') # escribir un mensaje
    figura = px.scatter(car_data, x="odometer") # crear un grafico de dispersion
    st.plotly_chart(figura, use_container_width=True) # mostrar un gráfico Plotly interactivo
    