"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_11():
    ruta="files/input/data.csv"
    resultado = {}
    with open(ruta, mode='r', encoding='utf-8', newline='') as archivo: 
        lector =csv.reader(archivo,delimiter='\t')
        for fila in lector:
            valor_columna_2 = int(fila[1].strip())
            valor_columna_3 = fila[3].strip().split(',')
            for clave in valor_columna_3:
                clave = clave.strip()
                if clave in resultado:
                    resultado[clave] += valor_columna_2
                else:
                    resultado[clave] = valor_columna_2
    resultado = dict(sorted(resultado.items()))
    return resultado
print ("Suma de la columna 2 para cada letra de la columna 3:", pregunta_11())

"""
Retorne un diccionario que contengan la suma de la columna 2 para cada
letra de la columna 3, ordenadas alfabeticamente.

Rta/
{'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


"""
