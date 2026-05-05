"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_10():
    ruta="files/input/data.csv"
    resultado = []
    with open(ruta, mode='r', encoding='utf-8', newline='') as archivo:
        lector =csv.reader(archivo,delimiter='\t')
        for fila in lector:
            letra = fila[0].strip()
            valor_columna_3 = fila[3].strip().split(',')
            valor_columna_4 = fila[4].strip().split(',')
            resultado.append((letra, len(valor_columna_3), len(valor_columna_4)))
    return resultado
print ("Letra de la columna 1 y cantidad de elementos de las columnas 3 y 4:", pregunta_10())

"""
Retorne una lista de tuplas contengan por cada tupla, la letra de la
columna 1 y la cantidad de elementos de las columnas 3 y 4.

Rta/
[('E', 3, 5),
    ('A', 3, 4),
    ...
    ('E', 2, 3),
    ('E', 3, 3)]


"""
