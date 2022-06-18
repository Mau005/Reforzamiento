import numpy as np
import random


def numeros_aleatorios(a, b):
    lista = np.array([])
    for x in range(a , b):
        lista = np.append(lista, random.randint(a,b))
    return lista


def imprimir_arrays(lista):
    for elementos in lista:
        print(elementos)
