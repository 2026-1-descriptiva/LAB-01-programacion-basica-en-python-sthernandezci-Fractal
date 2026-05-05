"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_08():
    ruta="files/input/data.csv"
    resultado = {}
    with open(ruta, mode='r', encoding='utf-8', newline='') as archivo:
        lector =csv.reader(archivo,delimiter='\t')
        for fila in lector:
            letra = fila[0].strip()
            valor = int(fila[1].strip())
            if valor in resultado:
                if letra not in resultado[valor]:
                    resultado[valor].append(letra)
            else:
                resultado[valor] = [letra]
    resultado = sorted([(valor, sorted(letras)) for valor, letras in resultado.items()])
    return resultado
print ("Asociacion entre columna 0 y columna 1 sin repetir letras:", pregunta_08())
"""
Genere una lista de tuplas, donde el primer elemento de cada tupla
contiene  el valor de la segunda columna; la segunda parte de la tupla
es una lista con las letras (ordenadas y sin repetir letra) de la
primera  columna que aparecen asociadas a dicho valor de la segunda
columna.

Rta/
[(0, ['C']),
    (1, ['B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E']),
    (4, ['B', 'E']),
    (5, ['B', 'C', 'D', 'E']),
    (6, ['A', 'B', 'C', 'E']),
    (7, ['A', 'C', 'D', 'E']),
    (8, ['A', 'B', 'D', 'E']),
    (9, ['A', 'B', 'C', 'E'])]

"""
