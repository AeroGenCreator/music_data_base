"""Agregar una cancion, memoria RAM"""
import streamlit as st


class NuevaPieza():
    """Esta clase pretende recibir la data de los usuarios
    para crear un diccionario por cancion"""

    def __init__(self,
                 cancion='Desconocido',
                 autor='Desconocido',
                 album='Desconocido',
                 genero='Desconocido',
                 fecha=-1, duracion=-1,
                 usuario_calificacion=0
                 ):

        self.cancion = cancion.title()
        self.autor = autor.title()
        self.album = album.title()
        self.genero = genero.title()
        self.fecha = fecha
        self.duracion = duracion
        self.usuario_calificacion = usuario_calificacion


def formulario_agregar_pieza():
    """Esta funcion muestra la interfaz de formulario
    y opera con los inputs para almacenarlos en un diccionario
    en RAM"""
    diccionario_cache = {
        'cancion': '',
        'autor': '',
        'album': '',
        'genero': '',
        'fecha': 0,
        'duracion': 0,
        'calificacion': 0,
    }
    # Codigo de la interfaz
    st.subheader('Formulario: Tu nueva pieza musical.')
    # Elementos de texto:
    cancion_de_usuario = st.text_input('Ingresar el nombre de la "Cancion":')
    autor_de_usuario = st.text_input('Ingresar el nombre del "Autor":')
    album_de_usuario = st.text_input('Ingresar el nombre del "Album":')
    genero_de_usuario = st.text_input('Ingresar un "Genero" para la cancion:')
    # Elementos numericos:
    fecha_de_usuario = st.number_input(
        'Ingresar el "Año de Lanzamiento" de la cancion (ej. 2023):',
        min_value=1000,
        step=1,
        format='%d')
    duracion_de_usuario = st.number_input(
        'Ingresar la "Duracion" de la cancion (ej. 1.25):',
        min_value=0.00,
        max_value=60.00,
        step=0.01,
        format='%.2f')
    calificacion_de_usuario = st.number_input(
        'Ingresar una "Calificacion" (ej. 9.8):',
        min_value=0.0,
        max_value=10.0,
        step=0.1,
        format='%.1f')

    usuario = NuevaPieza(
        cancion_de_usuario,
        autor_de_usuario,
        album_de_usuario,
        genero_de_usuario,
        fecha_de_usuario,
        duracion_de_usuario,
        calificacion_de_usuario
    )

    # Aqui mando la data a un diccionario limpio.
    diccionario_cache['cancion'] = usuario.cancion
    diccionario_cache['autor'] = usuario.autor
    diccionario_cache['album'] = usuario.album
    diccionario_cache['genero'] = usuario.genero
    diccionario_cache['fecha'] = usuario.fecha
    diccionario_cache['duracion'] = usuario.duracion
    diccionario_cache['calificacion'] = usuario.usuario_calificacion

    st.dataframe(diccionario_cache)
    return diccionario_cache
