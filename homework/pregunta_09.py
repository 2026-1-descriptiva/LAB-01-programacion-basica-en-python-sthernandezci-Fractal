"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_09():
    ruta="files/input/data.csv"
    resultado = {}
    with open(ruta, mode='r', encoding='utf-8', newline='') as archivo:
        lector =csv.reader(archivo,delimiter='\t')
        for fila in lector:
            diccionario = fila[4].strip()
            pares = diccionario.split(',')
            for par in pares:
                clave = par.split(':')[0].strip()
                if clave in resultado:
                    resultado[clave] += 1
                else:
                    resultado[clave] = 1
    resultado = dict(sorted(resultado.items()))
    return resultado
print ("Cantidad de registros por cada clave de la columna 4:", pregunta_09())


"""
Retorne un diccionario que contenga la cantidad de registros en que
aparece cada clave de la columna 4.

Rta/
{'aaa': 13,
    'bbb': 16,
    'ccc': 23,
    'ddd': 23,
    'eee': 15,
    'fff': 20,
    'ggg': 13,
    'hhh': 16,
    'iii': 18,
    'jjj': 18}}

"""
