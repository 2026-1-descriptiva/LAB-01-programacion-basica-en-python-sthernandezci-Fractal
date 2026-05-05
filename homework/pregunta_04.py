"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_04():
    ruta="files/input/data.csv"
    conteo = {}
    with open(ruta, mode='r', encoding='utf-8', newline='') as archivo:
        lector =csv.reader(archivo,delimiter='\t')
        for fila in lector:
            fecha = fila[2].strip()
            mes = fecha[5:7]  # Extraer el mes de la fecha
            if mes in conteo:
                conteo[mes] += 1
            else:
                conteo[mes] = 1
    resultado = sorted(conteo.items())
    return resultado
print ("Cantidad de registros por cada mes de la columna 3:", pregunta_04())

"""
La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
cantidad de registros por cada mes, tal como se muestra a continuación.

Rta/
[('01', 3),
    ('02', 4),
    ('03', 2),
    ('04', 4),
    ('05', 3),
    ('06', 3),
    ('07', 5),
    ('08', 6),
    ('09', 3),
    ('10', 2),
    ('11', 2),
    ('12', 3)]

"""
