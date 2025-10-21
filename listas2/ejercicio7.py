"""8. Realizar un programa que permita mediante un menú de opciones, las siguientes operaciones:
 a. Cargar 3 listas paralelas: nombre, legajo y nota que son los registros de los estudiantes hasta que el
 operador no quiera ingresar más datos, validar que las notas estén en el intervalo [0, 100]. El legajo no
 puede estar repetido. Utilice sub algoritmos para la validación.
 b. Mostrar los registros en el orden en que fueron ingresados u ordenados por nombre a opción del
 operador.
 c. Mostrar los registros cuyas notas superan al promedio ordenados de mayor a menor.
 d. Mostrar la nota máxima y mínima y cuántos estudiantes las obtuvieron.
 e. Agregar un nuevo registro.
 f. Agregar una nueva nota para todos los estudiantes.
 g. Modificar un registro ingresando el legajo del estudiante.
 h. Eliminar un estudiante ingresando el legajo.
 i.
 Salir
 Consideración: para poder realizar las opciones b, c, d, f, g,h se debe verificar que haya al menos un registro
 cargado, en caso contrario mostrar el mensaje "Debe cargar registros antes de realizar esta operación".
 También debe limpiar la pantalla cada vez que se termine de procesar una opción."""

import os

def menu_opciones():
    os.system('clear')
    print('a. Cargar 3 listas paralelas: nombre, legajo y nota')
    print('b. Mostrar los registros en el orden en que fueron ingresados u ordenados por nombre')
    print('c. Mostrar los registros cuyas notas superan al promedio ordenados de mayor a menor.')
    print('d. Mostrar la nota máxima y mínima y cuántos estudiantes las obtuvieron.')
    print('e. Agregar un nuevo registro.')
    print('f. Agregar una nueva nota para todos los estudiantes.')
    print('g. Modificar un registro ingresando el legajo del estudiante.')
    print('h. Eliminar un estudiante ingresando el legajo.')
    print('i. Salir')
    opcion=str(input('Elegir a, b, c, d, e, f, g, h o i: '))
    while opcion not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'):
        opcion=str(input('Debe elegir a, b, c, d, e, f, g, h o i: '))
    return opcion

def listas_paralelas():
    nombre=[]
    legajo=[]
    nota=[]
    continuar='s'
    while continuar=='s':
        nombre.append(str(input('Ingresar nombre estudiante: ').capitalize()))
        legajos=str(input('Ingrese legajo: ')).upper()
        while validar_legajo(legajos, legajo):
            legajos=str(input('Legajo invalido, ingrese nuevamente: '))
        legajo.append(legajos)
        notas=float(input('Ingrese nota: '))
        while validar_nota(notas):
            notas=float(input('Nota invalida, ingrese nuevamente: '))
        nota.append(notas)
        continuar=str(input('Desea continuar s o n: '))
    return nombre, legajo, nota

def validar_nota(nota):
    validar=False
    if nota < 0 or nota > 100:
        validar=True
    return validar

def validar_legajo(legajo, legajos):
    validar=False
    if legajo in legajos:
        validar=True
    return validar

def mostrar_listas(nombre, legajo, nota):
    mostrar=int(input('Mostrar lista por orden de ingreso (1) u ordenados por nombre (2): '))
    while mostrar not in (1, 2):
        mostrar=str(input('1 o 2: '))
    if mostrar==1:
        for i in range(len(legajo)):
            print(f'nombre: {nombre[i]}, legajo: {legajo[i]}, nota: {nota[i]}')
    elif mostrar==2:
        registros=list(zip(nombre, legajo, nota))
        registros.sort(key=lambda x: x[0])
        for nombre, legajo, nota in registros:
            print(f'nombre: {nombre}, legajo: {legajo}, nota: {nota}')

def notas_mayor_promedio(nombre, legajo, nota):
    acumulador=0
    for num in nota:
        acumulador+=num
    promedio=acumulador/len(nota)
    registros=list(zip(nombre, legajo, nota))
    registros.sort(key=lambda x: x[2], reverse=True)
    for nombre, legajo, nota in registros:
        if nota > promedio:
            print(f'nombre: {nombre}, legajo: {legajo}, nota: {nota}')

#PRINCIPAL
nombre=[]
legajo=[]
nota=[]

while True:
    opcion=menu_opciones()
    if opcion=='a':
        nombre, legajo, nota=listas_paralelas()
    elif opcion=='b':
        mostrar_listas(nombre, legajo, nota)
    elif opcion=='c':
        notas_mayor_promedio(nombre, legajo, nota)
    elif opcion=='i':
        print('Hasta luego...')
        break
    input('Presione enter para continuar...')