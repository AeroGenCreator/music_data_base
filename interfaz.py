"""Este codigo representa la interfaz de Usuario"""
import streamlit as st

# Modulos propios
import agregar_pieza
import memoria_rom

# Titulos
st.header('Stack\'M')
st.subheader("Tu base de datos musical")
st.write('Powered by Linux Mint')

# interacciones
agregar = st.checkbox('Agregar pieza musical 📀')
buscar_pieza = st.checkbox('Buscar en la Base de Datos')
mostrar_base_completa = st.checkbox('Mostrar toda tu Musica 🗄️')
casilla_formatear = st.checkbox('Formatear "Base de Datos" ⚠️')

# Ejecuciones de codigo
if agregar:
    pre_diccionario = agregar_pieza.formulario_agregar_pieza()
    aceptar_nueva_pieza = st.button('Aceptar para: Agregar')
    if aceptar_nueva_pieza:
        memoria_rom.agregar_al_room(pre_diccionario)
if buscar_pieza:
    st.write('En construccion')
if mostrar_base_completa:
    st.subheader('Base de Datos Musical ')
    st.subheader('🗃️')
    tabla = memoria_rom.acceso_a_rom()
    st.dataframe(tabla)
if casilla_formatear:
    st.subheader('En este menu podras eliminar toda tu informacion')
    st.subheader('⚠️')
    formateo = st.button('"Click para aceptar formateo"')
    if formateo:
        memoria_rom.reset_memoria_rom()
        st.chat_message("assistant")
        st.write('BASE DE DATOS FORMATEADA EXITOSAMENTE ⚙️')
        st.write('Recarga la pagina para ver los cambios')
        salir_formato = st.button('Recargar Pagina')
        if salir_formato:
            st.rerun()
