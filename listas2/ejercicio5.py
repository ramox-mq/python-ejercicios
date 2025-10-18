""" 6. Un club de pescadores realizó una competencia de pesca. Por cada participante se registrará la cantidad total
 de peces atrapados. Para ello, se tiene dos listas que almacenan el nombre del participante y las cantidades de
 peces por participante. Diseñar un algoritmo modular, que mediante un menú de opciones resuelve:
 1. Dar la bienvenida al concurso de pesca
 2. Cargar las listas con una cantidad n de participantes. La mínima cantidad de participantes es 10 y la
 máxima es 50. La cantidad de peces debe ser mayor o igual a 0.
 3. Mostrar el promedio de peces capturados.
 4. Mostrar la mayor cantidad de peces capturados y el nombre del ganador (pueden haber empates).
 5. Disminuir x peces al participante que está en la posición z.
 6. Despedirse y salir"""

import random

def menu_opciones():
    print('1. bienvenida')
    print('2. Cargar las listas con una cantidad n de participantes.')
    print('3. Mostrar el promedio de peces capturados.')
    print('4. Mostrar la mayor cantidad de peces capturados y el nombre del ganador (pueden haber empates).')
    print('5. Disminuir x peces al participante que está en la posición z.')
    print('6. Despedirse y salir')
    eleccion=int(input('Elegir 1, 2, 3, 4, 5, 6: '))
    while eleccion not in (1, 2, 3, 4, 5, 6):
        eleccion=int(input('Elegir 1, 2, 3, 4, 5, 6: '))
    return eleccion

def bienvenida():
    print('Concurso de peces!!!')

def cargar_lista_participantes():
    participantes=[]
    cantidad_participantes=int(input('Ingresar cantidad de participantes, entre [10, 50]: '))
    while cantidad_participantes < 10 or cantidad_participantes > 50:
        cantidad_participantes=int(input('entre [10, 50]: '))
    for i in range(cantidad_participantes):
        participantes.append(f'participante {i}')
    peces=[]
    for i in range(len(participantes)):
        peces.append(random.randint(0, 100))
    return participantes, peces

def promedio_peces(peces):
    acumulador=0
    for i in peces:
        acumulador+=i
    promedio=acumulador/len(peces)
    return promedio

def ganador(participantes, peces):
    mayor=peces[0]
    for i in range(len(participantes)):
        if peces[i] > mayor:
            mayor=peces[i]

    ganadores=[]

    for i in range(len(participantes)):
        if peces[i]==mayor:
            ganadores.append(participantes[i])
    return ganadores, mayor

def disminuir_peces_participante(participantes, peces):
    for i, participante in enumerate(participantes):
        print(i, participante)
    reducir_peces=int(input('Elegir indice de participante a disminuir cantidad de peces: '))
    cantidad=int(input('Cuantos peces quitar: '))
    if peces[reducir_peces] - cantidad >= 0:
        peces[reducir_peces] -= cantidad
    else:
        print('No puede tener cantidad negativa, no se realiza la resta')
    print(peces)

#PRINCIPAL
participantes=[]
peces=[]

while True:
    opcion=menu_opciones()
    if opcion==1:
        bienvenida()
    elif opcion==2:
        participantes, peces=cargar_lista_participantes()
        print(f'participantes: {participantes} \npeces: {peces}')
    elif opcion==3:
        promedio=promedio_peces(peces)
        print(f'Promedio de peces: {promedio}')
    elif opcion==4:
        ganadores, mayor=ganador(participantes, peces)
        print(f'ganador/es: {ganadores}, con {mayor} peces')
    elif opcion==5:
        disminuir_peces_participante(participantes, peces)
    elif opcion==6:
        print('Gracias por participar, adios...')
        break
    input('Presione enter para continuar...')