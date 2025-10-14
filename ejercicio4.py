""" 4. Diseñar un algoritmo que permita realizar lo siguiente:
 ● Cargar una lista con N números enteros
 ● Mostrar los números ingresados y su posición
 ● Mostrar si los elementos de la lista se encuentran ordenados en forma descendente
 ● Mostrar los valores que superen el promedio de los valores ingresados
 ● Mostrar el mínimo de los valores ingresados y su posición
 ● Indicar qué elementos son valores primos
 ● El algoritmo debe considerar que si no se cargó la lista previamente, no se pueda realizar alguna de las
 acciones solicitadas."""

def menu_opciones():
    print('1 Cargar la lista de números enteros')
    print('2 Mostrar los números ingresados y su posición')
    print('3 Mostrar si los elementos de la lista se encuentran ordenados en forma descendente')
    print('4 Mostrar los valores que superen el promedio de los valores ingresados')
    print('5 Mostrar el mínimo de los valores ingresados y su posición')
    print('6 Indicar qué elementos son valores primos')
    print('7 Salir')
    eleccion=int(input('1, 2, 3, 4, 5, 6 o 7: '))
    while eleccion not in (1, 2, 3, 4, 5, 6, 7):
        eleccion=int(input('Debe elegir opcion: 1, 2, 3, 4, 5, 6 o 7: '))
    return eleccion

def cargar_lista():
    cantidad_numeros=int(input('Ingresar cantidad de numeros: '))
    lista_numeros=[]
    for i in range(cantidad_numeros):
        numero=int(input('Ingrese numero: '))
        lista_numeros.append(numero)
    print('Carga de numeros completa')
    return lista_numeros

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
    numeros_mayores=[]
    acumulador=0
    cantidad_numeros=len(lista)
    for i in range(len(lista)):
        acumulador+=lista[i]
    promedio=acumulador/cantidad_numeros
    print('promedio', promedio)
    for i in range(len(lista)):
        if lista[i]>promedio:
            numeros_mayores.append(lista[i])
    print('mayores al promedio:')
    print(numeros_mayores)

def minimo_ingresado(lista):
    valor_minimo=lista[0]
    indice=0
    for i in range(len(lista)):
        if lista[i] < valor_minimo:
            valor_minimo=lista[i]
            indice=i
    print('valor minimo ingresado:', valor_minimo, 'i:', indice)

def valores_primos(lista):
    numeros_primos=[]
    for num in lista:
        if num > 1:
            es_primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
        if es_primo:
            numeros_primos.append(num)
    print('numeros primos de la lista')
    print(numeros_primos)

#PRINCIPAL
lista=[]
while True:
    opcion=menu_opciones()
    if opcion==1:
        lista=cargar_lista()
    if len(lista)==0:
        print('La lista está vacía, no se puede realizar esta acción')
        print('Debe cargar la lista para realizar esta acción')
        break
    elif opcion==2:
        mostrar_numeros(lista)
    elif opcion==3:
        orden_numeros(lista)
    elif opcion==4:
        mayores_promedio(lista)
    elif opcion==5:
        minimo_ingresado(lista)
    elif opcion==6:
        valores_primos(lista)
    elif opcion==7:
        break
    input('Presione enter para continuar...')