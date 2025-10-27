"""4. Escribir un programa que permita gestionar una base de datos de estudiantes de una carrera de la facultad. Los
estudiantes se guardan en un diccionario en el que la clave de cada cliente será su Libreta Universitaria (LU),

 los datos del estudiante son nombre, dirección, teléfono, correo, estado), donde el estado tendrá el valor True
si se trata de un estudiante activo. El programa debe preguntar al usuario por una opción del siguiente menú:
1. Añadir estudiante, por defecto estado True
2. Eliminar estudiante,
3. Mostrar estudiante,
4. Listar todos los estudiantes,
5. Listar estudiantes activos o pasivos (permitir la selección)
6. Cambiar de estado a un estudiante solicitando la LU (True a False o False a True)."""


def menu_opciones():
    print("1. Añadir estudiante, por defecto estado True")
    print("2. Eliminar estudiante")
    print("3. Mostrar estudiante")
    print("4. Listar todos los estudiantes")
    print("5. Listar estudiantes activos o pasivos (permitir la selección)")
    print(
        "6. Cambiar de estado a un estudiante solicitando la LU (True a False o False a True)."
    )
    print("7. Salir")
    opcion = int(input("1, 2, 3, 4, 5, 6, 7: "))
    while opcion not in (1, 2, 3, 4, 5, 6, 7):
        opcion = int(input("Elegir 1, 2, 3, 4, 5, 6, 7: "))
    return opcion


def agregar(estudiantes):
    while True:
        estudiante = {}
        lu = str(input("ingrese LU, 0 para salir: "))
        if lu == "0":
            break
        nombre = str(input("Ingresar nombre: ")).title()
        direccion = str(input("Ingrese direccion: "))
        telefono = int(input("Ingrese telefono: "))
        correo = str(input("Ingrese correo: "))
        estado = True
        estudiante.update(
            {
                "nombre": nombre,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo,
                "estado": estado,
            }
        )
        estudiantes.update({lu: estudiante})
    print(estudiantes)


def eliminar(estudiantes):
    lu = str(input("Ingrese libreta estudiante para eliminar: "))
    confirmar = str(input("Seguro de eliminar? s o n: "))
    if confirmar == "s":
        estudiantes.pop(lu)
    print(estudiantes)


def mostrar(estudiantes):
    lu = str(input("Ingrese libreta estudiante para mostrar: "))
    for estudiante in estudiantes:
        if estudiante == lu:
            print(f"estudiante: {estudiantes[estudiante]}")


def mostrar_estudiantes(estudiantes):
    print("Estudiantes:")
    print(estudiantes)


def mostrar_activos_pasivos(estudiantes):
    elegir = str(input("Mostrar (p)asivos o (a)ctivos: "))
    while elegir not in ("a", "p"):
        elegir = str(input("Mostrar (p)asivos o (a)ctivos: "))
    if elegir == "a":
        for estudiante in estudiantes:
            if estudiantes[estudiante]["estado"]:
                print(estudiantes[estudiante])
    elif elegir == "p":
        for estudiante in estudiantes:
            if not estudiantes[estudiante]["estado"]:
                print(estudiantes[estudiante])


def cambiar_estado(estudiantes):
    lu = str(input("Ingrese libreta estudiante para modificar estado: "))
    respuesta = input("¿El estudiante está activo? (s/n): ").lower()

    if respuesta == "s":
        estudiantes[lu]['estado'] = True
    else:
        estudiantes[lu]['estado'] = False

# PRINCIPAL
estudiantes = {
    "1001": {
        "nombre": "Ana Gómez",
        "direccion": "Av. San Martín 1234",
        "telefono": "351-4567890",
        "correo": "ana.gomez@email.com",
        "estado": True,
    },
    "1002": {
        "nombre": "Luis Pérez",
        "direccion": "Calle Belgrano 567",
        "telefono": "351-1234567",
        "correo": "luis.perez@email.com",
        "estado": True,
    },
    "1003": {
        "nombre": "Carla Díaz",
        "direccion": "Boulevard Illia 890",
        "telefono": "351-9876543",
        "correo": "carla.diaz@email.com",
        "estado": False,
    },
}

while True:
    opcion = menu_opciones()
    if opcion == 1:
        agregar(estudiantes)
    elif opcion == 2:
        eliminar(estudiantes)
    elif opcion == 3:
        mostrar(estudiantes)
    elif opcion == 4:
        mostrar_estudiantes(estudiantes)
    elif opcion == 5:
        mostrar_activos_pasivos(estudiantes)
    elif opcion == 6:
        cambiar_estado(estudiantes)
    elif opcion == 7:
        print("Adiós...")
        break
    input("Presione enter para continuar...")
