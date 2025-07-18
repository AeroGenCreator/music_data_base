"""Este codigo representa la interfaz de Usuario"""
import streamlit as stm
import agregar_pieza

stm.header('Tu Base de Datos Musical')
agregar = stm.checkbox('Agregar pieza musical')
if agregar:
    agregar_pieza.formulario_agregar_pieza()
    aceptar_nueva_pieza = stm.button('Aceptar para: Agregar')
