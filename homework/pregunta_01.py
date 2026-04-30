"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
from pathlib import Path

def pregunta_01():
    total=0
    ruta_csv = Path("files/input/data.csv")
    with ruta_csv.open(mode='r', encoding='utf-8',newline='') as archivo:
        lector =csv.reader(archivo, delimiter=';')
        
        for fila in lector:
            try:
                valor = int(fila[1].strip())
                total += valor
            except ValueError:
                continue
    print (f"\nTotal Final: {total}")
    return total

