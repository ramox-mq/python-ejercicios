"""7. Diseñar un programa modular que permita gestionar los productos de un comercio, las funcionalidades
 solicitadas son:
 1. Registrar productos: para cada uno se debe solicitar, código, descripción, precio y stock. Agregar las
 siguientes validaciones:
 a. El código no se puede repetir
 b. Todos los valores son obligatorios
 c. El precio y el stock no pueden ser negativos
 2. Mostrar el listado de productos
 3. Mostrar los productos cuyo stock sea menor a un valor dado
 4. Incrementar el stock de un producto
 5. Mostrar el producto de menor precio
 6. Buscar el precio más alto de la lista de productos y a continuación listar los productos que lo poseen."""

def registrar_productos():
    codigos=[]
    descripciones=[]
    precios=[]
    stocks=[]
    cantidad_productos=int(input('Ingresar cantidad de productos a registrar: '))
    for i in range(cantidad_productos):
        codigo=str(input('Ingresar codigo producto: '))
        while codigo in codigos or codigo=='':
            codigo=str(input('codigo invalido, ingrese nuevamente: '))
        descripcion=str(input('Ingresar descripcion producto: '))
        while descripcion=='':
            descripcion=str(input('Descripcion invalida, ingrese nuevamente: '))
        precio=float(input('Ingresar precio producto: '))
        while precio<=0:
            precio=float(input('Precio invalido, ingrese nuevamente: '))
        stock=int(input('Ingresar stock producto: '))
        while stock <=0:
            stock=int(input('Stock invalido, ingrese nuevamente: '))
        
        codigos.append(codigo)
        descripciones.append(descripcion)
        precios.append(precio)
        stocks.append(stock)
        input('Enter para continuar')
    print(codigos, descripciones, precios, stocks)
    mostrar_productos(codigos, descripciones, precios, stocks)

def mostrar_productos(codigos, descripciones, precios, stocks):
    for i in range(len(codigos)):
        print(f'producto {i+1}: {codigos[i]}, {descripciones[i]}, {precios[i]}, {stocks[i]}')

def stock_menor(stock):
    
    
registrar_productos()
