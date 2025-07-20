"""Este codigo representa la interfaz de Usuario"""
import streamlit as st

# Modulos propios
import agregar_pieza
import memoria_rom

# Titulos
st.header('Stack\'Em')
st.subheader("Tu base de datos musical 💽")

# interacciones
agregar = st.checkbox('Agregar pieza musical 📀')
mostrar_base_completa = st.checkbox('Mostrar toda tu Musica 🗄️')
casilla_formatear = st.checkbox('Formatear "Base de Datos" ⚠️')

# Ejecuciones de codigo
if agregar:
    pre_diccionario = agregar_pieza.formulario_agregar_pieza()
    aceptar_nueva_pieza = st.button('Aceptar para: Agregar')
    if aceptar_nueva_pieza:
        memoria_rom.agregar_al_room(pre_diccionario)
if mostrar_base_completa:
    tabla = memoria_rom.acceso_a_rom()
    st.dataframe(tabla)
if casilla_formatear:
    formateo = st.button('"Click para aceptar formateo"')
    if formateo:
        memoria_rom.reset_memoria_rom()
        st.chat_message("assistant")
        st.write('BASE DE DATOS FORMATEADA EXITOSAMENTE ⚙️')
        st.write('Recarga la pagina para ver los cambios')
        salir_formato = st.button('Recargar Pagina')
        if salir_formato:
            st.rerun()
