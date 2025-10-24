"""8. Escribir un módulo que reciba una cadena de unos y ceros (es decir, un número en representación binaria) y
 devuelva el valor decimal correspondiente."""

def unos_ceros(cad_binario):
    decimal=int(cad_binario, 2)
    return decimal

cad_binario=str(input('binario a decimal: '))

print(f'Equivalencia en decimal: {unos_ceros(cad_binario)}')