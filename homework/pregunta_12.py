"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_12():
    ruta="files/input/data.csv"
    resultado = {}
    with open(ruta, mode='r', encoding='utf-8', newline='') as archivo:
        lector =csv.reader(archivo,delimiter='\t')
        for fila in lector:
            letra = fila[0].strip()
            diccionario = fila[4].strip()
            pares = diccionario.split(',')
            for par in pares:
                valor_columna_4 = int(par.split(':')[1].strip())
                if letra in resultado:
                    resultado[letra] += valor_columna_4
                else:
                    resultado[letra] = valor_columna_4
        resultado = dict(sorted(resultado.items()))
    resultado = dict(sorted(resultado.items()))
    return resultado
print ("Suma de la columna 4 para cada letra de la columna 1:", pregunta_12())

"""
Genere un diccionario que contengan como clave la columna 1 y como valor
la suma de los valores de la columna 4 sobre todo el archivo.

Rta/
{'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

"""
