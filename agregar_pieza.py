"""Agregar una cancion, memoria RAM"""
# Librerias integradas
import datetime as dt
# Libreria de terceros
import streamlit as st


class NuevaPieza():
    """Esta clase pretende recibir la data de los usuarios
    para crear un diccionario por cancion"""

    def __init__(self,
                 cancion='Desconocido',
                 autor='Desconocido',
                 album='Desconocido',
                 genero='Desconocido',
                 fecha=-1,
                 duracion=dt.timedelta(minutes=1, seconds=1),
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
    st.subheader('💽')

    # Elementos de texto:
    cancion_de_usuario = st.text_input('Ingresar el nombre de la "Cancion":')
    autor_de_usuario = st.text_input('Ingresar el nombre del "Autor":')
    album_de_usuario = st.text_input('Ingresar el nombre del "Album":')
    genero_de_usuario = st.text_input('Ingresar un "Genero" para la cancion:')

    # Elementos numericos:
    fecha_de_usuario = st.number_input(
        'Ingresar el "Año de Lanzamiento" de la cancion (ej. 2023):',
        min_value=0000,
        step=1,
        format='%d')
    col1, col2 = st.columns(2)
    with col1:
        minutos_de_usuario = st.number_input(
            'Ingresa los minutos de la cancion',
            min_value=0,
            max_value=59,
            step=1,
            format='%d',
            key='registro_de_minutos'
        )
    with col2:
        segundos_de_usuario = st.number_input(
            'Ingresa los segundos de la cancion',
            min_value=0,
            max_value=59,
            step=1,
            format='%d',
            key='registro_de_segundos'
        )
    duracion_timedelta = dt.timedelta(
        minutes=minutos_de_usuario, seconds=segundos_de_usuario)
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
        duracion_timedelta,
        calificacion_de_usuario
    )

    # Aqui mando la data a un diccionario limpio.
    diccionario_cache['cancion'] = usuario.cancion
    diccionario_cache['autor'] = usuario.autor
    diccionario_cache['album'] = usuario.album
    diccionario_cache['genero'] = usuario.genero
    diccionario_cache['fecha'] = usuario.fecha
    diccionario_cache['duracion'] = str(usuario.duracion)[2:]
    diccionario_cache['calificacion'] = usuario.usuario_calificacion

    st.dataframe(diccionario_cache)
    return diccionario_cache
