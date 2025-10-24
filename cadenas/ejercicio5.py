""" 7. Escribir un módulo que tiene un parámetro que es una cadena de caracteres devuelve:La primera letra de
 cada palabra de la cadena en mayúsculas.Por ejemplo,si recibe “universal serial bus” debe devolver “USB”.
"""


def devolver_primera_letra(cadena):
    for cad in cadena:
        if cad.isupper():
            print(cad, end='')

            
cadena=str(input('Ingrese frase: ')).title()

devolver_primera_letra(cadena)