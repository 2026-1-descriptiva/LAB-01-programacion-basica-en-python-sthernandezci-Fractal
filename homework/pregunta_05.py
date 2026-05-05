"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_05():
    ruta="files/input/data.csv"
    resultado = {}
    with open(ruta, mode='r', encoding='utf-8', newline='') as archivo:
        lector =csv.reader(archivo,delimiter='\t')
        for fila in lector:
            letra = fila[0].strip()
            valor = int(fila[1].strip())
            if letra in resultado:
                maximo, minimo = resultado[letra]
                resultado[letra] = (max(maximo, valor), min(minimo, valor))
            else:
                resultado[letra] = (valor, valor)
    resultado = sorted([(letra, maximo, minimo) for letra, (maximo, minimo) in resultado.items()])
    return resultado
print ("Valor maximo y minimo de la columna 2 por cada letra de la primera columna:", pregunta_05())
"""
Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
por cada letra de la columa 1.

Rta/
[('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

"""
