import pandas as pd
import plotly.express as px
import streamlit as st

st.markdown("<h1 style='text-align: center;'>Analisis de Vehiculos</h1>", unsafe_allow_html=True)

# =================== Cargar datos ===================
df = pd.read_csv('vehicles_us.csv')

# Copia original por si no se filtra
df_filtrado = df.copy()

# =================== SIDEBAR DE FILTROS ===================
st.sidebar.title("Filtros")

# --- Filtro por año ---
rango_anios = st.sidebar.slider(
    "Año del modelo:",
    min_value=1990,
    max_value=2025,
    value=(2000, 2020),
    step=1
)

# --- Filtro por transmisión ---
transmisiones = st.sidebar.multiselect(
    "Tipo de transmisión:",
    options=sorted(df['transmission'].dropna().unique()),
    default=[]
)

# --- Filtro por tipo de vehículo ---
tipos = st.sidebar.multiselect(
    "Tipo de vehículo:",
    options=sorted(df['type'].dropna().unique()),
    default=[]
)

# --- Botón para aplicar los filtros ---
aplicar_filtros = st.sidebar.button("Aplicar todos los filtros")

# =================== APLICAR FILTROS ===================
if aplicar_filtros:
    df_filtrado = df[
        (df['model_year'] >= rango_anios[0]) &
        (df['model_year'] <= rango_anios[1])
    ]

    if transmisiones:
        df_filtrado = df_filtrado[df_filtrado['transmission'].isin(transmisiones)]

    if tipos:
        df_filtrado = df_filtrado[df_filtrado['type'].isin(tipos)]

# =================== TABLA COMPLETA ===================
st.header("Tabla de Datos:")
st.dataframe(df_filtrado)

# =================== PRECIO PROMEDIO POR MODELO ===================
table2 = df_filtrado.groupby("model")["price"].mean().reset_index()
st.header("Precio promedio por modelo")
st.dataframe(table2)

fig1 = px.bar(table2, x='model', y='price', title='Grafica de barras de modelo por precio')
st.plotly_chart(fig1)

# =================== ODOMETRO PROMEDIO POR AÑO ===================
table3 = df_filtrado.groupby("model_year")["odometer"].mean().reset_index()
st.header("Kilometraje promedio por año del modelo")
st.dataframe(table3)

fig3 = px.scatter(table3, x='model_year', y='odometer', title='' \
'Grafica de dispercion del modelo del año por kilometraje')
st.plotly_chart(fig3)