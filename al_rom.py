"""Este codigo interactua en con archivos JSON"""
# Libreria local
import json
# Libreria de terceros
import streamlit as stm


def agregar_al_room(diccionario: dict):
    """Aqui agrego a la base de datos permanente"""
    json_file = open('base_de_datos.json', 'w', encoding='utf-8')
    json.dump(diccionario, json_file, indent=2, ensure_ascii=False)
    # ensure.ascii=False (permite que los simbolos o caracteres especiales se mantengan)
    with stm.chat_message("user"):
        stm.write('Pieza Agregada. 👍🏼')
