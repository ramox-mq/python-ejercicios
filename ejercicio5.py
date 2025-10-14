"""Diseñar un algoritmo que permita realizar lo siguiente:
 ● Cargar una lista con valores de tipo caracter a pedido del operador.
 ● Mostrar la lista desde el último valor ingresado hasta el primero.
 ● Solicitar un valor al usuario y buscar en la lista devolviendo la posición del primer valor encontrado. En
 caso que no se encuentre devolver-1
 ● Indicar la cantidad de vocales de la lista"""

def elegir_opcion():
    print('1 Cargar una lista con valores de tipo caracter a pedido del operador.')
    print('2 Mostrar la lista desde el último valor ingresado hasta el primero.')
    print('3 Solicitar un valor al usuario y buscar en la lista devolviendo la posición del primer valor encontrado. En caso que no se encuentre devolver-1')
    print('4 Indicar la cantidad de vocales de la lista')
    print('5 Salir')
    elegir=int(input('1, 2, 3, 4 o 5: '))
    while elegir not in (1, 2, 3, 4, 5):
        elegir=int(input('Debe ser 1, 2, 3, 4 o 5: '))
    return elegir

def cargar_lista():
    continuar='s'
    lista_caracteres=[]
    while continuar=='s':
        agregar=str(input('Ingrese el valor a insertar en la lista: '))
        lista_caracteres.append(agregar.lower())
        print('Valor cargado correctamente')
        continuar=str(input('Desea continuar? s o n: '))
    return lista_caracteres

def mostrar_lista(lista):
    print(lista[::-1])

def contar_vocales(lista):
    contador=0
    for i in range(len(lista)):
        if lista[i].lower() in ('a', 'i', 'e', 'o', 'u'):
            contador+=1
    print('vocales:', contador)

def buscar_usuario(lista):
    valor=str(input('Ingrese valor a encontrar en la lista: ')).lower()
    if valor not in lista:
        print('-1')
    else:
        print('elemento encontrado en la posición:', lista.index(valor))

#PRINCIPAL
lista_caracteres=[]
while True:
    opcion=elegir_opcion()
    if opcion==1:
        lista_caracteres=cargar_lista()
    elif opcion==2:
        mostrar_lista(lista_caracteres)
    elif opcion==3:
        buscar_usuario(lista_caracteres)
    elif opcion==4:
        contar_vocales(lista_caracteres)
    elif opcion==5:
        break
    input('Presione enter para continuar...')