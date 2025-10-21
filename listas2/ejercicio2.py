"""1. Realizar un programa modular que permita cargar en forma aleatoria una matriz cuadrada (número de filas
 igual a número de columnas ingresado por el usuario) con valores enteros entre 100 a 200 incluidos. Mostrar el
 valor máximo de cada columna, el valor mínimo de cada fila, el promedio de los valores que componen la
 diagonal principal, finalmente, pase a una lista los valores que se repiten y muestre las mismas."""

import random

def cargar_lista():
    orden_matriz=int(input('Ingrese el orden de la matriz cuadrada: '))
    matriz=[]
    for i in range(orden_matriz):
        fila = []
        for j in range(orden_matriz):
            fila.append(random.randint(100,200))
        matriz.append(fila)
    print(matriz)
    maximo_columnas(matriz)
    minimo_filas(matriz)
    promedio_diagonal(matriz)
    valores_repetidos(matriz)

def maximo_columnas(matriz):
    lista_max_col=[]
    for col in range(len(matriz[0])):
        max_col=matriz[0][col]
        for fila in range(len(matriz)):
            if max_col < matriz[fila][col]:
                max_col=matriz[fila][col]
        lista_max_col.append(max_col)
    print(lista_max_col)

def minimo_filas(matriz):
    lista_min_filas=[]
    for filas in matriz:
        min_fila=filas[0]
        for fila in filas:
            if fila < min_fila:
                min_fila=fila
        lista_min_filas.append(min_fila)
    print(lista_min_filas)

def promedio_diagonal(matriz):
    acumulador=0
    for i, filas in enumerate(matriz):
        for j, num in enumerate(filas):
            if i==j:
                acumulador+=num
    promedio=acumulador/len(matriz)
    print(promedio)

def valores_repetidos(matriz):
    lista_repetidos=[]
    for filas in matriz:
        for num in filas:
            if filas.count(num) > 1 and num not in lista_repetidos:
                lista_repetidos.append(num)
    print(lista_repetidos)


cargar_lista()