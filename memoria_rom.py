"""Este codigo interactua en con archivos JSON"""
# Libreria local
import json
import os
# Libreria de terceros
import streamlit as st
import pandas as pd

FILE_PATH = 'base_de_datos.json'


def reset_memoria_rom():
    """Este bloque formatea la base de datos y agrega una
    lista vacia en json"""
    if os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0:
        try:
            with open(FILE_PATH, 'w', encoding='utf-8') as new_file:
                data = []
                json.dump(data, new_file)
        except json.JSONDecodeError:
            st.write('Error al formatear la lista')


def agregar_al_room(diccionario: dict):
    """Aqui agrego a la base de datos permanente"""
    lista_cache = []
    # Verificar que el archi esxisate y no esta vacio:
    if os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0:
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as json_file:
                # Si no esta vacio procedemos a la lectura:
                data = json_file.read()
                # Eliminamos tabulaciones:
                if data.strip():
                    # Se carga a la lista cache si todo resulta un exito:
                    lista_cache = json.loads(data)
                # De aqui en adelante es manejo de errores:
                else:
                    st.write(
                        f'El archivo "{FILE_PATH}" está vacío o contiene solo espacios')
                    st.write('Se iniciara una lista vacia para tus datos.')
        except json.JSONDecodeError:
            st.write(
                f'Error: El archivo "{FILE_PATH}" no es un formato JSON válido.')
            st.write('Se inicializará como una lista vacía.')
            lista_cache = []
        except ImportError as e:
            st.write(f"Ocurrió un error al leer el archivo '{FILE_PATH}': {e}")
            lista_cache = []
    # Me aseguro que el contenido en archivo json sea una lista:
    if not isinstance(lista_cache, list):
        st.write(f'El archivo "{FILE_PATH}" no es una lista.')
        st.write('Se iniciara una lista vacia')
        lista_cache = []
    # Agrego el nuevo diccionario:
    lista_cache.append(diccionario)
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as json_file:
            json.dump(lista_cache, json_file, indent=4, ensure_ascii=False)
            st.chat_message("assistant")
            st.write('PIEZA AGREGADA EXITOSAMENTE 💽')
    except ImportError as e:
        st.write(
            f'Ocurrio un error al escibir el archivo "{FILE_PATH}". Error: {e}')


def acceso_a_rom():
    """De aqui se importa json a un DataFrame"""
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        data_json = json.load(file)
        df = pd.DataFrame(data=data_json)
        return df


def borrar_pieza_del_rom():
    """Esta funcion pretende localizar una cancion
    y borrarla de la memoria principal:"""
