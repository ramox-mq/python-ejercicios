"""2. Escribir un programa que implemente una agenda con diccionarios. En la agenda se podrán guardar nombres y
números de teléfono. El programa debe mostrar el siguiente menú:
1. Añadir/modificar: solicita un nombre, si el nombre se encuentra en la agenda, debe mostrar el
teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe
permitir ingresar el teléfono correspondiente.
2. Buscar: solicitando una cadena de caracteres, y muestra todos los contactos cuyos nombres comienzan
por dicha cadena.
3. Borrar: solicita un nombre y si existe nos preguntará si queremos borrarlo de la agenda. Si existe más
de uno debe identificarlos por un número secuencial que permita al usuario identificarlo para realizar
la operación de borrado.
4. Listar: muestra todos los contactos de la agenda."""

import os


def menu_opciones():
    os.system("cls")
    print("1. Añadir/modificar: solicita un nombre")
    print(
        "2. Buscar: solicitando una cadena de caracteres, y muestra todos los contactos cuyos nombres comienzan por dicha cadena."
    )
    print(
        "3. Borrar: solicita un nombre y si existe nos preguntará si queremos borrarlo de la agenda."
    )
    print("4. Listar: muestra todos los contactos de la agenda.")
    print("5. Salir.")
    opcion = int(input("Opcion 1, 2, 3, 4 o 5: "))
    while opcion not in (1, 2, 3, 4, 5):
        opcion = int(input("Elegir 1, 2, 3, 4 o 5: "))
    return opcion


def generar_agenda():
    agendas = {}
    indice = 0
    continuar = "s"
    while continuar == "s":
        contacto = {}
        nombre = str(input("Ingrese nombre: ")).title()
        if not validar_nombre(agendas, nombre):
            telefono = int(input("Ingrese nro. de telefono: "))
            contacto.update({"Nombre": nombre, "Telefono": telefono})
            agendas[f"Contacto {indice}"] = contacto
            indice += 1

        continuar = str(input("continuar agregando/modificando? s o n: "))
    print(agendas)
    return agendas


def validar_nombre(agendas, nombre):
    validar = False
    for i in agendas:
        if agendas[i].get("Nombre") == nombre:
            telefono=agendas[i].get('Telefono')
            print(f'telefono: {telefono}')
            modif_numero(telefono, agendas[i])
            validar = True
    return validar

def modif_numero(telefono, usuario):
    preg_modif=str(input('Quiere modificar el número? s o n: '))
    if preg_modif == 's':
        nuevo_telefono=int(input('Ingrese nuevo nro. de telefono: '))
        usuario['Telefono']=nuevo_telefono

def mostrar_contactos_car(agendas):
    buscar_cadena=str(input('Buscar por cadena: ')).capitalize()
    encontrado=False
    for a in agendas:
        if agendas[a]['Nombre'].startswith(buscar_cadena):
            encontrado=True
            print(a, agendas[a])

    if not encontrado:
        print(f'No se encontro a ningun contacto que empieze con: {buscar_cadena}')
    
def borrar_contacto(agenda):
    print(agenda)
    borrar_contacto=str(input('Indique cual contacto borrar: ')).capitalize()
    agenda.pop(borrar_contacto)
    print('Se elimino el contacto')
    print(agenda)

def mostrar_agenda(agenda):
    print(agenda)
            
    

        



# PRINCIPAL
agendas={}
while True:
    opcion = menu_opciones()
    if opcion==1:
        agendas=generar_agenda()
    elif opcion==2:
        mostrar_contactos_car(agendas)
    elif opcion==3:
        borrar_contacto(agendas)
    elif opcion==4:
        mostrar_agenda(agendas)
    elif opcion == 5:
        print("Adiós...")
        break
    input("Presione enter para continuar...")
