"""Diseñar un algoritmo que permita realizar lo siguiente:
 ● Cargar una lista con valores numéricos hasta que el usuario ingrese cero. No debe permitir que se
 carguen valores duplicados en la lista.
 ● Mostrar la lista completa con la cantidad de elementos
 ● Agregar un elemento al final de la lista
 ● Insertar un elemento preguntando la posición al usuario. Valide que el valor no se encuentre cargado.
 ● Eliminar un elemento indicado por el usuario. Si no se encuentra debe informar con un mensaje.
 ● Copiar los valores pares a otra lista de nombre listaPares. Mostrar ambas listas."""

def elegir_operacion():
    print('1 Cargar una lista con valores numéricos hasta que el usuario ingrese cero.')
    print('2 Mostrar la lista completa con la cantidad de elementos')
    print('3 Agregar un elemento al final de la lista')
    print('4 Insertar un elemento preguntando la posición al usuario.')
    print('5 Eliminar un elemento indicado por el usuario.')
    print('6 Copiar los valores pares a otra lista de nombre listaPares. Mostrar ambas listas.')
    print('7 Salir')
    elegir=int(input('1, 2, 3, 4, 5, 6 o 7: '))
    while elegir not in (1, 2, 3, 4, 5, 6, 7):
        elegir=int(input('1, 2, 3, 4, 5, 6 o 7: '))
    return elegir

def cargar_lista():
    lista_numeros=[]
    cargar_numero=int(input('Ingrese el valor a cargar en la lista, 0 para salir: '))
    while cargar_numero != 0:
        if validar_numero_lista(lista_numeros, cargar_numero):
            lista_numeros.append(cargar_numero)
        else:
            print('El número ya fue ingresado en la lista, no se guarda...')
        cargar_numero=int(input('Ingrese el valor a cargar en la lista, 0 para salir: '))
    return lista_numeros

def validar_numero_lista(lista, numero):
    validar=False
    if numero not in lista:
        validar=True
    return validar

def mostrar_lista(lista):
    cantidad_elementos=len(lista)
    for i, elem in enumerate(lista):
        print(f'i:{i}, elem:{elem},')
    print(f'cantidad elementos: {cantidad_elementos}')

def agregar_elemento(lista):
    nuevo_elemento=int(input('Ingrese elemento a agregar a la lista: '))
    if validar_numero_lista(lista, nuevo_elemento):
        lista.append(nuevo_elemento)
    else:
        print('El número ya esta en la lista... no se guarda...')
    return lista

def agregar_numero_posicion(lista):
    numero_nuevo=int(input('Ingrese elemento a agregar a la lista: '))
    posicion=int(input('Indicar en que posicion colocar el numero en la lista: '))
    if validar_numero_lista(lista, numero_nuevo):
        lista.insert(posicion, numero_nuevo)
    else:
        print('Numero ya en la lista, no se agrega...')

def eliminar_elemento(lista):
    eliminar=int(input('Indique que elemento quiere eliminar: '))
    if eliminar in lista:
        lista.remove(eliminar)
    else:
        print(f'El elemento a eliminar, {eliminar}, no se encuentra en la lista')

def nueva_lista_pares(lista):
    lista_pares=[]
    for i in lista:
        if i%2==0:
            lista_pares.append(i)
    mostrar_listas(lista, lista_pares)

def mostrar_listas(lista1, lista2):
    print(f'lista de numero ingresados: \n {lista1}')
    print(f'lista de numeros pares copiados de la lista principal: \n {lista2}')



#PRINCIPAL
lista_numeros=[]
while True:
    opcion=elegir_operacion()
    if opcion==1:
        lista_numeros=cargar_lista()
    elif opcion==2:
        mostrar_lista(lista_numeros)
    elif opcion==3:
        agregar_elemento(lista_numeros)
    elif opcion==4:
        agregar_numero_posicion(lista_numeros)
    elif opcion==5:
        eliminar_elemento(lista_numeros)
    elif opcion==6:
        nueva_lista_pares(lista_numeros)
    elif opcion==7:
        break
    input('Presionar enter para continuar...')
