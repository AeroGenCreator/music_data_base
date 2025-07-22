"""Este codigo buscara por cancion, album, genero, año, u artista."""

#librerias de python
import json
# Mis modulos
import memoria_rom
# librerias de terceros
import pandas as pd

df = memoria_rom.acceso_a_rom()
print(df)