""" 3. Ingrese un texto y cuente las cantidades de repeticiones para los caracteres que lo componen. Ejemplo de
 entrada: INTRODUCCION A LA PROGRAMACION y salida:"""

ingresar_texo=str(input('ingresar texto: ')).upper()

diccionario={}
for cad in ingresar_texo:
    if cad in diccionario:
        diccionario[cad] += 1
    else:
        diccionario[cad] = 1
    

print(diccionario)

