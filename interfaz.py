"""Este codigo representa la interfaz de Usuario"""
import streamlit as st

# Modulos propios
import agregar_pieza
import memoria_rom

# Titulos
st.header('Stack\'Em')
st.subheader("Tu base de datos musical 💽")

agregar = st.checkbox('Agregar pieza musical')
mostrar_base_completa = st.checkbox('Mostrar toda tu Musica')

if agregar:
    pre_diccionario = agregar_pieza.formulario_agregar_pieza()
    aceptar_nueva_pieza = st.button('Aceptar para: Agregar')
    if aceptar_nueva_pieza:
        memoria_rom.agregar_al_room(pre_diccionario)

if mostrar_base_completa:
    tabla = memoria_rom.acceso_a_rom()
    st.dataframe(tabla)
