""" 4. Diseñar un algoritmo que permita realizar lo siguiente:
 ● Cargar una lista con N números enteros
 ● Mostrar los números ingresados y su posición
 ● Mostrar si los elementos de la lista se encuentran ordenados en forma descendente
 ● Mostrar los valores que superen el promedio de los valores ingresados
 ● Mostrar el mínimo de los valores ingresados y su posición
 ● Indicar qué elementos son valores primos
 ● El algoritmo debe considerar que si no se cargó la lista previamente, no se pueda realizar alguna de las
 acciones solicitadas."""

def cargar_lista():
    cantidad_numeros=int(input('Ingresar cantidad de numeros: '))
    lista_numeros=[]
    for i in range(cantidad_numeros):
        numero=int(input('Ingrese numero: '))
        lista_numeros.append(numero)
    print(lista_numeros)
    mostrar_numeros(lista_numeros)
    orden_numeros(lista_numeros)
    mayores_promedio(lista_numeros)

def mostrar_numeros(lista):
    for i, numero in enumerate(lista):
        print(f'i: {i}, num: {numero}')
    
def orden_numeros(lista):
    for i in range(len(lista)-1):
        validar=False
        if lista[i] >= lista[i+1]:
            validar=True
    if validar:
        print('La lista esta ordenada de forma descendente')
    else:
        print('La lista no esta ordenada de foroma descendente')

def mayores_promedio(lista):
    acumulador=0
    cantidad_numeros=len(lista)
    for i in range(len(lista)):
        acumulador+=lista[i]
    promedio=acumulador/cantidad_numeros
    print('promedio', promedio)
    for i in range(len(lista)):
        if lista[i]>promedio:
            print(lista[i], end=' ')


cargar_lista()