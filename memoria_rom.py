"""Este codigo interactua en con archivos JSON"""
# Libreria local
import json
# Libreria de terceros
import streamlit as st
import pandas as pd

FILE_PATH = 'base_de_datos.json'


def agregar_al_room(diccionario: dict):
    """Aqui agrego a la base de datos permanente"""
    with open(FILE_PATH, 'r+', encoding='utf-8') as json_file:
        data = json.load(json_file)
        data = data.append(diccionario)
        json.dump(data, json_file, indent=2, ensure_ascii=False)
        st.chat_message("assistant")
        st.write('PIEZA AGREGADA EXITOSAMENTE 💽')


def acceso_a_rom():
    """De aqui se importa json a un DataFrame"""
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        data_json = json.load(file)
        data_json = [data_json]
        df = pd.DataFrame(data=data_json)
        return df
