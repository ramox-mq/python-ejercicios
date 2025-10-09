def menu_opciones():
    print('a. Registrar estudiantes')
    print('b. Mostrar el listado de estudiantes con sus respectivas notas.')
    print('c. Buscar a un estudiante por su DNI y mostrar su nombre y nota.')
    print('d. Modificar los datos de un estudiante buscando por DNI (el DNI no se puede modificar).')
    print('e. Eliminar a un estudiante buscando por DNI. Emitir un mensaje de confirmación.')
    print('f. Mostrar el promedio de las notas ingresadas')
    print('g. Salir')
    eleccion=str(input('a, b, c, d, e, f, o g')).lower()
    while eleccion not in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
        eleccion=str(input('Debe ser a, b, c, d, e, f o g'))
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

def validar_nota(nota):
    validar=False
    if nota < 0 or nota > 10:
        validar=True
    return validar


#Principal
