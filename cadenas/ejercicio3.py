""" 5. Ingresar una frase por teclado, se desea modificar todos los espacios en blanco dobles y dejar solo un espacio
 en blanco."""

frase=str(input('Ingresar una frase: '))
while '  ' in frase:
    frase=frase.replace('  ', ' ').strip()

print(frase)