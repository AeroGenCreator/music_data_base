"""librerias"""

lista_cache = []


def agregar_cancion():
    """recibe el nombre de una cancion"""
    cancion = input()
    try:
        cancion = cancion.lower().title().replace('-', ' ').replace('_', ' ')
        return cancion
    except ValueError:
        return


def agregar_genero():
    """recibe un genero musical (libre eleccion)"""
    genero = input()
    try:
        genero = genero.lower().title().replace('-', ' ').replace('_', ' ')
        return genero
    except ValueError:
        return


def agregar_autor():
    """recibe el nombre de un autor"""
    autor = input()
    try:
        autor = autor.lower().title().replace('-', ' ').replace('_', ' ')
        return autor
    except ValueError:
        return


diccionario_cache = {
    'cancion': '',
    'genero': '',
    'autor': '',
}

cancion_cache = agregar_cancion()
diccionario_cache['cancion'] = cancion_cache

genero_cache = agregar_genero()
diccionario_cache['genero'] = genero_cache

autor_cache = agregar_autor()
diccionario_cache['autor'] = autor_cache

lista_cache.append(diccionario_cache)
print(lista_cache)
