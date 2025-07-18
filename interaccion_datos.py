"""librerias"""

lista_cache = []


def agregar_cancion():
    """recibe el nombre de una cancion"""
    cancion = input()
    try:
        cancion = cancion.lower().replace(' ', '_')
        return cancion
    except ValueError:
        return


diccionario_cache = {'cancion': ''}

cancion_cache = agregar_cancion()
diccionario_cache['cancion'] = cancion_cache
lista_cache.append(diccionario_cache)

print(lista_cache)
