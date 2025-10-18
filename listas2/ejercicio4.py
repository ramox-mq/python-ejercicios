"""5. Realizar un módulo suma_fc_mat(tabla, c, k) que devuelve un número que es la suma de una fila o columna y
 es del mismo tipo de dato de la matriz, los parámetros son una lista de listas denominada tabla, un parámetro
 de tipo string denominado c que si tiene el valor ‘f’ se sumará una fila y si tiene el valor ‘c’ se sumará una
 columna, finalmente hay un parámetro entero denominado k que indica qué fila o columna se desea sumar."""

def suma_fc_mat(tabla, c, k):
    if c =='f':
        acumulador=0
        fila_elegida=tabla.pop(k)
        for num in fila_elegida:
            acumulador+=num
        return acumulador
    elif c == 'c':
        acumulador=0
        for filas in tabla:
            acumulador+=filas[k]
        return acumulador



tabla=[
    [5,4,7,3],
    [4,8,9,7],
    [5,1,2,3],
    [4,1,2,9],
    [6,7,8,0]
    ]
c='c'
k=1

print(suma_fc_mat(tabla, c, k))