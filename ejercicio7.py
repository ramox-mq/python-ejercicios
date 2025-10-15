"""Escribir el código que permita:
 ● Cargar una lista con N valores aleatorios (random.randint(a,b)), los valores aleatorios deben
 encontrarse entre 0 y 100. El valor N es el tamaño de la lista ingresado por el usuario.
 ● Mostrar el sector de la lista deseada, ingresar el inicio el fin y el paso.
 ● Copiar la lista a una denominada listaInversa en donde el orden de los elementos se encuentra en
 orden inverso a la lista original. Muestre ambas listas.
 ● Eliminar de listaInversa los valores duplicados. Mostrar ambas listas"""

import random

def menu_opciones():
    print('1 Cargar una lista con N valores aleatorios')
    print('2 Mostrar el sector de la lista deseada, ingresar el inicio el fin y el paso.')
    print('3 Copiar la lista a una denominada listaInversa en donde el orden de los elementos se encuentra en orden inverso a la lista original.')
    print('4 Eliminar de listaInversa los valores duplicados.')
    print('5 Salir')
    eleccion=int(input('Elegir opcion 1, 2, 3, 4 o 5: '))
    while eleccion not in (1, 2, 3, 4, 5):
        eleccion=int(input('Debe elegir 1, 2, 3, 4 o 5: '))
    return eleccion

def cargar_lista_aleatoria():
    lista_aleatoria=[]
    largo_lista=int(input('Ingrese tamaño de la lista: '))
    for i in range(largo_lista):
        lista_aleatoria.append(random.randint(0,100))
    print(lista_aleatoria)
    return lista_aleatoria

def mostrar_sector_lista(lista):
    inicio=int(input('Inicio: '))
    paso=int(input('Paso: '))
    fin=int(input('Fin: '))
    print(lista[inicio:fin+1:paso])

def copiar_lista(lista):
    lista_inversa=lista[::-1]
    print(f'lista copiada orden inverso: \n {lista_inversa}')
    print(f'lista original \n {lista}')
    return lista_inversa

def eliminar_lista_inversa(listaInversa):
    lista_valores_unicos=[]
    for i in listaInversa:
        if i not in lista_valores_unicos:
            lista_valores_unicos.append(i)
    print(f'Lista con elementos duplicados eliminados:\n {lista_valores_unicos}')
    print(f'Lista inversa original: \n {listaInversa}')

#PRINCIPAL
lista_aleatoria=[]
lista_inversa=[]
while True:
    opcion=menu_opciones()
    if opcion==1:
        lista_aleatoria=cargar_lista_aleatoria()
    elif opcion==2:
        mostrar_sector_lista(lista_aleatoria)
    elif opcion==3:
        lista_inversa=copiar_lista(lista_aleatoria)
    if len(lista_aleatoria)==0:
        print('No se puede hacer esta accion hasta que se eliga opcion 3')
        break
    elif opcion==4:
        eliminar_lista_inversa(lista_inversa)
    elif opcion==5:
        break
    input('Presione enter para continuar...')