"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_06():
    ruta="files/input/data.csv"
    resultado = {}  
    with open(ruta, mode='r', encoding='utf-8', newline='') as archivo:
        lector =csv.reader(archivo,delimiter='\t')
        for fila in lector:
            diccionario = fila[4].strip()
            pares = diccionario.split(',')
            for par in pares:
                clave, valor = par.split(':')
                clave = clave.strip()
                valor = int(valor.strip())
                if clave in resultado:
                    minimo, maximo = resultado[clave]
                    resultado[clave] = ( min(minimo, valor),max(maximo, valor))
                else:
                    resultado[clave] = (valor, valor)
    resultado = sorted([(clave, minimo, maximo) for clave, (minimo, maximo) in resultado.items()])
    return resultado
print ("Valor maximo y minimo de la columna 5 por cada clave:", pregunta_06())

"""
La columna 5 codifica un diccionario donde cada cadena de tres letras
corresponde a una clave y el valor despues del caracter `:` corresponde al
valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
pequeño y el valor asociado mas grande computados sobre todo el archivo.

Rta/
[('aaa', 1, 9),
    ('bbb', 1, 9),
    ('ccc', 1, 10),
    ('ddd', 0, 9),
    ('eee', 1, 7),
    ('fff', 0, 9),
    ('ggg', 3, 10),
    ('hhh', 0, 9),
    ('iii', 0, 9),
    ('jjj', 5, 17)]

"""
