"""Diseñar un programa que, mediante un menú de opciones nos permite realizar:
 1. Generar N ternas de valores en forma aleatoria y agregarlas a una lista. Validar que los valores dentro
 de cada terna no se repitan.
 2. Mostrar la lista de valores generados
 3. Calcular la suma de todos los valores generados
 4. Calcular la suma de los valores de una terna a elección del usuario
 5. Calcular el promedio de una columna (primera, segunda o tercera) de las ternas a elección del usuario
 6. Salir"""

import random

def menu_opciones():
    print('1. Generar N ternas de valores en forma aleatoria y agregarlas a una lista.')
    print('Mostrar la lista de valores generados')
    print('3. Calcular la suma de todos los valores generados')
    print('4. Calcular la suma de los valores de una terna a elección del usuario')
    print('5. Calcular el promedio de una columna (primera, segunda o tercera) de las ternas a elección del usuario')
    print('6 Salir.')
    eleccion=int(input('1, 2, 3, 4, 5 o 6: '))
    while eleccion not in (1, 2, 3, 4, 5, 6):
        eleccion(int(input('Debe ser 1, 2, 3, 4, 5 o 6: ')))
    return eleccion

def generar_ternas():
    lista_ternas=[]
    cantidad_ternas=int(input('Cantidad de ternas a generar: '))
    for i in range(cantidad_ternas):    
        terna=[]
        while len(terna) < 3:
            numero_random = random.randint(0, 100)
            if validar_repeticion_lista(terna, numero_random):
                terna.append(numero_random)
                print('terna',terna)
        lista_ternas.append(terna)
    print(lista_ternas)

def validar_repeticion_lista(lista, numero):
    validar=True
    if numero in lista:
        validar=False
    return validar










#PRINCIPAL
while True:
    opcion=menu_opciones()
    if opcion==1:
        generar_ternas()
    elif opcion==6:
        break

