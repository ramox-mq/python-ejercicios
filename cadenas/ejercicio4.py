"""6. Solicitar el ingreso de una palabra clave por teclado. Controlar que la cadena ingresada tenga más de 6
 caracteres y almenos un número y un caracter en mayúsculas para que sea válido,en caso contrario mostrar
 un mensaje de error."""

clave=str(input('ingrese palabra clave: '))
tiene_numero=False
for i in range(len(clave)):
    if clave[i].isdigit():
        tiene_numero=True

if len(clave)<6:
    print('Debe tener mas de 6 caracteres')
elif no
