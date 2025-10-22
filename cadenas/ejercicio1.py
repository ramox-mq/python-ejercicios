"""1. Una institución bancaria tiene una aplicación que recibe una lista con los movimientos de las cuentas bancarias
 de sus clientes mediante un servicio externo. Para cada cuenta se recibe el número de cuenta, nombre y
 apellido del cliente, importe, fecha del movimiento y el tipo de movimiento (E=Extracción, D=Depósito). El
 formato de cada cuenta está dado por una cadena de caracteres donde cada atributo de una cuenta se
 encuentra separado por comas.
 Por ejemplo:
 27200123456,MARIA FERNANDEZ,0000500000,30-05-2021,E
 27200321654,CARLOS TORRES,0000400045,31-05-2021,D
 27200987125,LAURA AQUINO,0000230000,30-05-2021,D
 27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E
 27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E
 27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D 
  Tenga en cuenta que:
Los 2 últimos dígitos del importe corresponden a los centavos, o sea que el valor 0000500000 es
 equivalente a 5000 pesos.
La fecha solo tiene carácter informativo por lo que debe guardarse como un string.
 Se solicita lo siguiente:
 1. Procesar la lista recibida y guardar los datos recibidos en una lista.
 2. Mostrar la lista con las cuentas obtenidas.
 3. Mostrar los movimientos correspondientes a depósitos y el total acumulado.
 4. Mostrar los movimientos de una cuenta.
 Nota: utilice los datos del ejemplo para validar el programa"""

def procesar(lista):
    lista_car=[]
    for car in lista:
        movimiento=car.split(',')
        importe = movimiento[2]
        importe = float(importe[:-2] + '.' + importe[-2:])
        movimiento[2] = importe
        lista_car.append(movimiento)
    mostrar_movimientos(lista_car)
    depositos_total(lista_car)
    mostrar_cuenta(lista_car)

def mostrar_movimientos(lista):
    print('Movimientos')
    for i, listas in enumerate(lista):
        print(i, listas)
    
def depositos_total(lista):
    acumulador=0
    for listas in lista:
        if listas[4]=='D':
            acumulador+=listas[2]
            print(f'movimientos depositos: {listas}')
    print(f'Todal depositos: {acumulador}')

def mostrar_cuenta(lista):
    buscar_movimiento=str(input('Ingrese numero de cuenta a buscar: '))
    encontrado=False
    for listas in lista:
        if listas[0]==buscar_movimiento:
            print(f'Movimiento asociado a nro. de cuenta: {listas}')
            encontrado=True
    if not encontrado:
        print('No hay movimiento asociado a nro. de cuenta')

        

listaExterna = ["27200123456,MARIA FERNANDEZ,0000500056,30-05-2021,E",
                "27200321654,CARLOS TORRES,0000400045,31-05-2021,D",
                "27200987125,LAURA AQUINO,0000230000,30-05-2021,D",
                "27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E",
                "27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E",
                "27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D"]

procesar(listaExterna)