"""Agregar una cancion, memoria RAM"""

diccionario_cache = {
    'cancion': '',
    'autor': '',
    'album': '',
    'genero': '',
    'fecha': 0,
    'duracion': 0,
    'calificacion': 0,
}


class NuevaPieza():
    """Esta clase pretende recibir la data de los usuarios
    para crear un diccionario por cancion"""

    def __init__(self,
                 cancion='Desconocido',
                 autor='Desconocido',
                 album='Desconocido',
                 genero='Desconocido',
                 fecha=-1, duracion=-1,
                 usuario_calificacion=0
                 ):

        self.cancion = cancion.title()
        self.autor = autor.title()
        self.album = album.title()
        self.genero = genero.title()
        self.fecha = fecha
        self.duracion = duracion
        self.usuario_calificacion = usuario_calificacion


def al_diccionario():
    """Aqui mando la data a un diccionario limpio"""
    diccionario_cache['cancion'] = usuario.cancion
    diccionario_cache['autor'] = usuario.autor
    diccionario_cache['album'] = usuario.album
    diccionario_cache['genero'] = usuario.genero
    diccionario_cache['fecha'] = usuario.fecha
    diccionario_cache['duracion'] = usuario.duracion
    diccionario_cache['calificacion'] = usuario.usuario_calificacion


cancion_de_usuario = input('Ingresar el nombre de la "Cancion":')

autor_de_usuario = input('Ingresar el nombre del "Autor":')

album_de_usuario = input('Ingresar el nombre del "Album":')

genero_de_usuario = input('Ingresar un "Genero" para la cancion:')

fecha_de_usuario = input('Ingresar el "Año de Lanzamiento" de la cancion:')
try:
    fecha_de_usuario = int(fecha_de_usuario)
except ValueError:
    print('Ingresa "Numeros Enteros" unicamente.')
    print('Solo el Año')

duracion_de_usuario = input('Ingresar la "Duracion" de la cancion:')
try:
    duracion_de_usuario = float(duracion_de_usuario)
    decimal_duracion = duracion_de_usuario % 1
    if 0.0 > decimal_duracion > 0.59:
        print('El formato decimal ingresado es incorrecto')
        print('Formato debe ser mayor a 00.00')
        print('Y menor a 00.59')
except ValueError:
    print('Ingresa unicamente numeros en formato:')
    print('00.00')
calificacion_de_usuario = input('Ingresar una "Calificacion":')
try:
    calificacion_de_usuario = float(calificacion_de_usuario)
    decimal_calificacion = float(calificacion_de_usuario)
    entero_calificacion = calificacion_de_usuario - decimal_calificacion
    if 0 > entero_calificacion > 10:
        print('Tu calificacion puede ir de una escala de 1 a 10')
    else:
        if 0.0 > decimal_calificacion > 0.99:
            print('Con decimales de 0.0 a 0.99')
except ValueError:
    print('La calificacion debe ser un numero entre 0 y 10')


usuario = NuevaPieza(
    cancion_de_usuario,
    autor_de_usuario,
    album_de_usuario,
    genero_de_usuario,
    fecha_de_usuario,
    duracion_de_usuario,
    calificacion_de_usuario
)


al_diccionario()

if __name__ == '__main__':
    print(diccionario_cache)
