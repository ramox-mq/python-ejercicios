"""Hacer un programa que calcule el promedio de los valores de las medidas de los aforos, tener en cuenta que el
 vacío o null no cuenta para el cálculo. también debe mostrar los aforos con valor vacío"""

def promedio_aforos():
    acumulador=0
    total=0
    contador=0
    aforos = [7.5, 0.0, None, 8.2, 6.9, None, 8.5]
    for i in range(len(aforos)):
        if aforos[i] is not None:
            total+=1
            acumulador+=aforos[i]
        else:
            contador+=1
        
    promedio=acumulador/total
    print(acumulador)
    print(contador)
    print(total)
    print(round(promedio, 4))

promedio_aforos()