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
    print('2. Mostrar la lista de valores generados')
    print('3. Calcular la suma de todos los valores generados')
    print('4. Calcular la suma de los valores de una terna a elección del usuario')
    print('5. Calcular el promedio de una columna (primera, segunda o tercera) de las ternas a elección del usuario')
    print('6. Salir.')
    eleccion=int(input('1, 2, 3, 4, 5 o 6: '))
    while eleccion not in (1, 2, 3, 4, 5, 6):
        eleccion=(int(input('Debe ser 1, 2, 3, 4, 5 o 6: ')))
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
        lista_ternas.append(terna)
    return lista_ternas

def validar_repeticion_lista(lista, numero):
    validar=True
    if numero in lista:
        validar=False
    return validar

def mostrar_lista(lista):
    print(lista)

def sumar_valores_lista(lista):
    acumulador=0
    for listas in lista:
        for num in listas:
            acumulador+=num       
    print(acumulador)

def sumar_valores_terna(lista):
    acumulador=0
    copia_lista=lista.copy()
    for i in range(len(lista)):
        print(f'i:{i}, tupla:{lista[i]}')
    indice_terna=int(input('Elegir indice de tupla a sumar: '))
    terna_elegida=copia_lista.pop(indice_terna)
    for num in terna_elegida:
        acumulador+=num
    print(acumulador)

def promedio_columnas_lista(lista):  
    acumulador=0
    for listas in lista:
        print(listas)
    columna_elegida=int(input('Elegir columna 1, 2, 3, para calcular el promedio: '))
    while columna_elegida not in (1, 2, 3):
        columna_elegida=int(input('Solo tiene 3 columnas: '))
    for listas in lista:
        acumulador+=listas[columna_elegida-1]
    promedio=acumulador/len(lista)
    print(promedio)


#PRINCIPAL
lista_ternas=[]
while True:
    opcion=menu_opciones()
    if opcion==1:
        lista_ternas=generar_ternas()
    elif len(lista_ternas) == 0 and opcion in (2, 3, 4, 5):
        print('Lista vacía, por favor cárguela antes de realizar esta operación.')
    elif opcion==2:
        mostrar_lista(lista_ternas)
    elif opcion==3:
        sumar_valores_lista(lista_ternas)
    elif opcion==4:
        sumar_valores_terna(lista_ternas)
    elif opcion==5:
        promedio_columnas_lista(lista_ternas)
    elif opcion==6:
        break
    input('Presione enter para continuar...')

