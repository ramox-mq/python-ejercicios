""" 1. Mediante un menú de opciones realizar el siguiente programa modular para gestionar el listado de notas de un
 examen para los estudiantes de una institución educativa:
 1. Registrar estudiantes: para cada uno se debe solicitar DNI, nombre y nota. Validar que la nota se
 encuentre entre 0 y 10. El proceso finaliza cuando se ingresa un DNI igual a cero.
 2. Mostrar el listado de estudiantes con sus respectivas notas.
 3. Buscar a un estudiante por su DNI y mostrar su nombre y nota.
 4. Modificar los datos de un estudiante buscando por DNI (el DNI no se puede modificar).
 5. Eliminar a un estudiante por su DNI. Emitir un mensaje de confirmación.
 6. Mostrar los estudiantes que obtuvieron nota mayor o igual a una dada y el promedio correspondiente."""
import os

def menu_opciones():
    os.system('cls')
    print('1. Registrar estudiantes: para cada uno se debe solicitar DNI, nombre y nota.')
    print('2. Mostrar el listado de estudiantes con sus respectivas notas.')
    print('3. Buscar a un estudiante por su DNI y mostrar su nombre y nota.')
    print('4. Modificar los datos de un estudiante buscando por DNI (el DNI no se puede modificar).')
    print('5. Eliminar a un estudiante por su DNI. Emitir un mensaje de confirmación.')
    print('6. Mostrar los estudiantes que obtuvieron nota mayor o igual a una dada y el promedio correspondiente.')
    print('7. Salir.')
    opcion=int(input('Opcion 1, 2, 3, 4, 5, 6 o 7: '))
    while opcion not in (1, 2, 3, 4, 5, 6, 7):
        opcion=int(input('Elegir opcion 1, 2, 3, 4, 5, 6 o 7'))
    return opcion

def registrar_estudiantes():
    estudiantes={}
    i=0
    while True:
        estudiante={}
        dni=int(input('Ingresar DNI (solo números), 0 para salir: '))
        if dni==0:
            print('Adiós...')
            break
        nombre=str(input('Ingrese nombre estudiante: ')).title()
        nota=float(input('Ingrese nota estudiante: '))
        estudiante.update({
            'DNI': dni,
            'Nombre': nombre,
            'Nota': nota
        })
        estudiantes[f'estudiante {i}']=estudiante
        i+=1
    return estudiantes

def mostrar_estudiantes(registro_estudiantes):
    for estudiante, datos in registro_estudiantes.items():
        print(estudiante, datos)

def buscar_estudiante(estudiantes):
    buscar_dni=int(input('Ingrese dni estudiante a buscar: '))
    nro_estudiante=''
    for estudiante in estudiantes:
        if estudiantes[estudiante]['DNI'] == buscar_dni:
            nro_estudiante=estudiante
            print(nro_estudiante, estudiantes[estudiante])
    return nro_estudiante

def modificar_datos_estudiante(estudiantes):
    estudiante=buscar_estudiante(estudiantes)
    modif_nombre=str(input('Ingrese nuevo nombre: ')).title()
    modif_nota=float(input('Ingrese nueva nota: '))
    estudiantes[estudiante].update({
        'Nombre': modif_nombre,
        'Nota': modif_nota
        })
    print(estudiantes)

def eliminar_estudiante(estudiantes):
    estudiante=buscar_estudiante(estudiantes)
    confirmar=str(input(f'Eliminar al estudiante {estudiantes[estudiante]['Nombre']} s o n: '))
    if confirmar=='s':
        estudiantes.pop(estudiante)
        print('Se elimino al estudiante')
    else:
        print('No se elimina al estudiante')
    print(estudiantes)

def mostrar_notas(estudiantes):
    notas=len(estudiantes)
    notas_mayores=0
    nota_dada=float(input('Mostrar notas mayores a: '))
    for estudiante in estudiantes:
        if estudiantes[estudiante]['Nota']>=nota_dada:
            notas_mayores+=1
            print(estudiantes[estudiante].items())
    promedio=notas_mayores*100/notas
    print(f'Promedio de mayores sobre nota: {promedio}')




#PRINCIPAL
estudiantes={}

while True:
    opcion=menu_opciones()
    if opcion==1:
        estudiantes=registrar_estudiantes()
    elif opcion==2:
        mostrar_estudiantes(estudiantes)
    elif opcion==3:
        buscar_estudiante(estudiantes)
    elif opcion==4:
        modificar_datos_estudiante(estudiantes)
    elif opcion==5:
        eliminar_estudiante(estudiantes)
    elif opcion==6:
        mostrar_notas(estudiantes)
    elif opcion==7:
        print('Adiós...')
        break
    input('Presionar enter para continuar...')