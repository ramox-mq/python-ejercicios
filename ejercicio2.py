""" Escriba la función mayores_que(x, lista_valores) que cuente cuántos valores en la lista valores son mayores que
 x, por ejemplo mayores_que(5, [7, 3, 6, 0, 4, 5, 10]) devuelve el valor 3"""

def mayores_que(x, lista_valores):
    contador=0
    for i in range(len(lista_valores)):
        if lista_valores[i] > x:
            contador+=1
    print(contador)

mayores_que(9, [7, 3, 6, 0, 4, 5, 10])