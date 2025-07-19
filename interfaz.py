"""Este codigo representa la interfaz de Usuario"""
import streamlit as stm

# Modulos propios
import agregar_pieza
import al_rom

# Titulos
stm.header('A-BaseMusic')
stm.subheader("Tu base de datos musical")

agregar = stm.checkbox('Agregar pieza musical')
if agregar:
    pre_diccionario = agregar_pieza.formulario_agregar_pieza()
    aceptar_nueva_pieza = stm.button('Aceptar para: Agregar')
    if aceptar_nueva_pieza:
        al_rom.agregar_al_room(pre_diccionario)
