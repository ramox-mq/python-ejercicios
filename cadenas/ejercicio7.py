"""9. Escribir un módulo denominado ins_car_xd(cadena, car, x, d), devuelve una cadena que inserta un caracter en
 la cadena cada x cantidad de caracteres de la cadena, siendo el parámetro d la dirección desde dónde se
 comienza la inserción, d puede ser “i” o “f”, si d es “i” es desde el inicio y si d es “f” es desde el fin, por
 defecto d = “i” si no se especifica este parámetro . Ejemplo: cadena = “2552552550” car = “.” y x = 3 el
 módulo debería devolver “255.255.255.0” otro ejemplo cadena = “1234567890” car = “,” x = 3 y d = “f” el
 módulo debería devolver “1,234,567,890”"""

def ins_car_xd(cadena, car, x, d="i"):
    
    if d == "f":
        cadena = cadena[::-1]

    print(cadena)

    nueva = ""
    contador = 0

    for c in cadena:
        nueva += c
        contador += 1

        if contador == x:
            nueva += car
            contador = 0

    if nueva.endswith(car):
        nueva = nueva[:-1]
    if d == "f":
        nueva = nueva[::-1]
    
    return nueva

cadena="2552552550"
car = "."
x = 3

print(ins_car_xd(cadena, car, x))
#print(ins_car_xd(cadena, car, x, 'f'))