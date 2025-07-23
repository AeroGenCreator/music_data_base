"""Este codigo buscara por cancion, album, genero, año, u artista."""

#librerias de python
import json
# Mis modulos
import memoria_rom
# librerias de terceros
import pandas as pd
import streamlit as st

# Aqui ya se cargo el DataFrame desde JSON
df = memoria_rom.acceso_a_rom()

def buscar_cancion():
    """Interfaz y logica de busqueda"""
    user_cancion = st.text_input('Nombre de Cancion').title().strip()
    confirmar_cancion = st.button('Buscar')
    if confirmar_cancion:
        try:
            df_cancion = df[df['cancion'] == user_cancion]
            st.dataframe(df_cancion)
        except ValueError:
            st.write(f'No se encontro {user_cancion} en la base de datos.')

def buscar_autor():
    """Interfaz y logica de busqueda"""
    user_artista = st.text_input('Nombre de Artista').title().strip()
    confirmar_artista = st.button('Buscar')
    if confirmar_artista:
        try:
            df_artista = df[df['autor'] == user_artista]
            st.dataframe(df_artista)
        except ValueError:
            st.write(f'No se encontro {user_artista} en la base de datos.')

def buscar_genero():
    """Interfaz y logica de busqueda"""
    user_genero = st.text_input('Genero').title().strip()
    confirmar_genero = st.button('Buscar')
    if confirmar_genero:
        try:
            df_genero = df[df['genero'] == user_genero]
            st.dataframe(df_genero)
        except ValueError:
            st.write(f'No se encontro {user_genero} en la base de datos.')

def buscar_epoca():
    """Interfaz y logica de busqueda"""
    user_tiempo = st.number_input('Año',format='%d', step=1)
    confirmar_tiempo = st.button('Buscar')
    if confirmar_tiempo:
        try:
            df_tiempo = df[df['fecha'] == user_tiempo]
            st.dataframe(df_tiempo)
        except ValueError:
            st.write(f'No se encontro {user_tiempo} en la base de datos.')