"""6. Solicitar el ingreso de una palabra clave por teclado. Controlar que la cadena ingresada tenga más de 6
 caracteres y almenos un número y un caracter en mayúsculas para que sea válido,en caso contrario mostrar
 un mensaje de error."""

clave=str(input('ingrese palabra clave: '))
validar_caracteres=True
if len(clave)<6:
    validar_caracteres=False
    print('tiene +6 caracteres?', validar_caracteres)
else:
    print('Tiene +6 caracteres?', validar_caracteres)

validar_numero=False
for i in range(len(clave)):
    if clave[i].isdigit():
        validar_numero=True
        print('tiene numero?', validar_numero)
        break
if not validar_numero:
    print('Tiene numero?', validar_numero)

validar_mayus=False
for i in range(len(clave)):
    if clave[i].isupper():
        validar_mayus=True
        print('tiene mayuscula?', validar_mayus)
        break
if not validar_mayus:
    print('tiene mayuscula?', validar_mayus)

if not validar_caracteres or not validar_numero or not validar_mayus:
    print('La clave debe tener mas de 6 caracteres, un numero y una letra en mayuscula')
else:
    print('Clave valida')