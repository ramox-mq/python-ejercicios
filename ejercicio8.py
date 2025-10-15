""" Desarrolle una función llamada desviacion_estandar(lista_valores) de una muestra de una población cuyo
 parámetro valores sea una lista de números reales. La función debe retornar la desviación estándar de los
 valores:"""

import random

def generar_lista_random():
    lista_random=[]
    cantidad_elementos=int(input('Cuantos elementos quiere en la lista: '))
    for i in range(cantidad_elementos):
        lista_random.append(random.randint(0,100))
    return lista_random

def promedio_lista(lista):
    acumulador=0
    for i in lista:
        acumulador+=i
    promedio=acumulador/len(lista)
    print(f'promedio {promedio}')
    return promedio

def resta_promedio(lista, promedio):
    resta=[]
    for i in lista:
        cuadrado=(i - promedio)**2
        resta.append(cuadrado)
    print(f'resta: {resta}')
    return resta

def sumar_obtenido(lista):
    acumulador_obtenidos=0
    for i in lista:
        acumulador_obtenidos+=i
    print(f'sumar": {acumulador_obtenidos}')
    return acumulador_obtenidos

def dividir_cantidad(obtenido, lista):
    dividir=obtenido/len(lista)-1
    print(f'dividir: {dividir}')
    return dividir

def raiz_cuadrada(dividirObtenido):
    resultado=(dividirObtenido)**(1/2)
    return resultado

lst = [4.0, 1.0, 11.0, 13.0, 2.0, 7.0]

def desviacion_estandar(lista_valores):
    promedio=promedio_lista(lista_valores)
    resta_prom=resta_promedio(lista_valores, promedio)
    sumar_obtenidos=sumar_obtenido(resta_prom)
    dividir=dividir_cantidad(sumar_obtenidos, lista_valores)
    resultado=raiz_cuadrada(dividir)
    print('Desviación estandar:')
    print(round(resultado, 4))

desviacion_estandar(lst)