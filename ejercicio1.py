def menu_opciones():
    print('a. Registrar estudiantes')
    print('b. Mostrar el listado de estudiantes con sus respectivas notas.')
    print('c. Buscar a un estudiante por su DNI y mostrar su nombre y nota.')
    print('d. Modificar los datos de un estudiante buscando por DNI (el DNI no se puede modificar).')
    print('e. Eliminar a un estudiante buscando por DNI. Emitir un mensaje de confirmación.')
    print('f. Mostrar el promedio de las notas ingresadas')
    print('g. Salir')
    eleccion=str(input('a, b, c, d, e, f, o g: ')).lower()
    while eleccion not in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
        eleccion=str(input('Debe ser a, b, c, d, e, f o g: '))
    return eleccion

def registrar_estudiante():
    datos_estudiantes=[]
    while True:
        DNI=int(input('DNI estudiante: '))
        if DNI==0:
            break
        nombre=str(input('Nombre estudiante: '))
        nota=float(input('Nota del estudiante: '))
        while validar_nota(nota):
            nota=float(input('La nota debe estar entre [0, 10]: '))
        datos_estudiantes.append([DNI, nombre, nota])
        print()
        print('Registrar otro estudiante')
    return datos_estudiantes

def validar_nota(nota):
    validar=False
    if nota < 0 or nota > 10:
        validar=True
    return validar

def mostrar_estudiantes(lista):
    for i in range(len(lista)):
        print(lista[i])
        
def buscar_dni(lista):
    dni=int(input('Ingrese dni de estudiante a buscar: '))
    for i in range(len(lista)):
        if lista[i][0]==dni:
            estudiante=lista[i]
    return estudiante

def modificar_datos_estudiante(lista):
    modificar=buscar_dni(lista)
    preguntar_nombre=str(input('Desea modificar el nombre? s o n: '))
    if preguntar_nombre=='s':
        modificar[1]=str(input('Ingrese nuevo nombre del estudiante: '))
    preguntar_nota=str(input('Desea modificar la nota s o n: '))
    if preguntar_nota=='s':
        modificar[2]=float(input('Ingrese nueva nota del estudiante: '))
    print(modificar)

def eliminar_estudiante(lista):
    estudiante=buscar_dni(lista)
    preguntar_eliminar=str(input('Esta seguro de eliminar al estudiante? s o n: '))
    if preguntar_eliminar=='s':
        lista.remove(estudiante)
    print(lista)

def promedio_notas(lista):
    acumulador=0
    contador=len(lista)
    for i in range(len(lista)):
        acumulador+=lista[i][2]
    promedio=acumulador/contador
    return promedio




#Principal
continuar='s'
while continuar!='n':
    opcion=menu_opciones()
    if opcion=='a':
        print('Registrar estudiantes')
        datos_estudiantes=registrar_estudiante()
    elif opcion=='b':
        datos_estudiantes=[[46891118, "Daniel", 6], [45894589, "ramos", 6], [45838998, "mira", 8]]
        print('Mostrando listado de estudiantes con sus respectivas notas')
        mostrar_estudiantes(datos_estudiantes)
    elif opcion=='c':
        datos_estudiantes=[[46891118, "Daniel", 6], [45894589, "ramos", 6], [45838998, "mira", 8]]
        estudiante=buscar_dni(datos_estudiantes)
        print(estudiante)
    elif opcion=='d':
        datos_estudiantes=[[46891118, "Daniel", 6], [45894589, "ramos", 6], [45838998, "mira", 8]]
        modificar_datos_estudiante(datos_estudiantes)
    elif opcion=='e':
        datos_estudiantes=[[46891118, "Daniel", 6], [45894589, "ramos", 6], [45838998, "mira", 8]]
        eliminar_estudiante(datos_estudiantes)
    elif opcion=='f':
        datos_estudiantes=[[46891118, "Daniel", 6], [45894589, "ramos", 6], [45838998, "mira", 8]]
        promedio=promedio_notas(datos_estudiantes)
        print('Promedio de las notas de los estudiantes')
        print(promedio)
    elif opcion=='g':
        continuar=str(input('desea continuar? s o n: '))
    input('Presione enter para continuar')