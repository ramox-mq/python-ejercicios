""" 5. Utilizando diccionarios diseñar un programa modular que permita gestionar los productos de un comercio, las
 funcionalidades solicitadas son:

 a. Registrar productos: para cada uno se debe solicitar, código, descripción, precio y stock. Agregar las
 siguientes validaciones:
 i. El código no se puede repetir
 ii. Todos los valores son obligatorios
 iii. El precio y el stock no pueden ser negativos
 
 b. Mostrar el listado de productos

 c. Mostrar los productos cuyo stock se encuentre en el intervalo [desde, hasta]

 d. Diseñar un proceso que le sume X al stock de todos los productos cuyo valor actual de stock sea menor
 al valor Y.

 e. Eliminar todos los productos cuyo stock sea igual a cero.

 f. Salir"""


def menu():
    print('1. Registrar productos')
    print('2. Mostrar el listado de productos')
    print('3. Mostrar los productos cuyo stock se encuentre en el intervalo [desde, hasta]')
    print('4. sume X al stock de todos los productos cuyo valor actual de stock sea menor al valor Y.')
    print('5. Eliminar todos los productos cuyo stock sea igual a cero.')
    print('6. Salir')
    opcion=int(input('1, 2, 3, 4, 5, 6: '))
    while opcion not in (1, 2, 3, 4, 5, 6):
        opcion=int(input('1, 2, 3, 4, 5, 6: '))
    return opcion

def registrar_producto():
    productos={}
    while True:
        producto={}
        codigo=int(input('Ingrese codigo producto, 0 para salir: '))
        if codigo==0:
            break
        while codigo in productos:
            codigo=int(input('Invalido, Ingrese codigo producto, 0 para salir: '))
        descripcion=str(input('Descripcion producto: '))
        while len(descripcion)==0:
            descripcion=str(input('Invalido, Descripcion producto: '))
        precio=float(input('Precio producto: '))
        while precio<=0:
            precio=float(input('Invalido, Precio producto: '))
        stock=int(input('Stock producto: '))
        while stock<0:
            stock=int(input('Invalido, Stock producto: '))
        producto.update({
            'descripcion': descripcion,
            'precio': precio,
            'stock': stock
        })
        productos[codigo]=producto
    return productos

def mostrar_intervalo(productos):
    desde=int(input('Mostrar stock de productos desde: '))
    hasta=int(input('Mostrar stock productos hasta: '))
    for prod in productos:
        if productos[prod]['stock']>desde and productos[prod]['stock']<hasta:
            print(productos[prod])
        
def sumar_stocks(productos):
    sumar=int(input('Cantidad sumar a todos stocks: '))
    stock=int(input('Indique cantidad de stock a sumar: '))
    for prod in productos:
        if productos[prod]['stock']<stock:
            productos[prod]['stock']+=sumar
    print(productos)

def eliminar(productos):
    eliminar=[]
    for prod in productos:
        if productos[prod]['stock']==0:
            eliminar.append(prod)
    for i in range(len(eliminar)):
        productos.pop(eliminar[i])
    print(productos)

#PRINCIPAL  

productos={}
while True:
    opcion=menu()
    if opcion==1:
        productos=registrar_producto()
    elif opcion==2:
        print(productos)
    elif opcion==3:
        mostrar_intervalo(productos)
    elif opcion==4:
        sumar_stocks(productos)
    elif opcion==5:
        eliminar(productos)
    elif opcion==6:
        print('Adiós...')
        break


