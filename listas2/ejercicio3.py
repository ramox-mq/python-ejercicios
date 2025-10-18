""" 3. Cargar una matriz de NxN aleatoriamente y mostrar los valores de la diagonal principal."""
import random

def cargar_matriz():
    orden_matriz=int(input('Indicar orden de la matriz cuadrada: '))
    matriz=[]
    for i in range(orden_matriz):
        fila=[]
        for j in range(orden_matriz):
            fila.append(random.randint(0,100))
        matriz.append(fila)
    print(matriz)
    diagonal_matriz(matriz)

def diagonal_matriz(matriz):
    print('valores de la diagonal principal:')
    for i, filas in enumerate(matriz):
        for j, num in enumerate(filas):
            if i == j:
                print(num)


cargar_matriz()