""" 10. Hacer un módulo que acepte una cadena original y devuelve otra cadena que es el geringoso de la cadena
 original. Utilizar una iteración sobre la cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda
 luego de cada vocal de la cadena original."""

def modif_cadena(cad_original):
    nueva = ""
    for i in range(len(cad_original)):
        nueva+=cad_original[i]
        if cad_original[i]=='a':
            nueva+='pa'
        
        if cad_original[i]=='o':
            nueva+='po'
        
        if cad_original[i]=='u':
            nueva+='pu'

        if cad_original[i]=='e':
            nueva+='pe'

        if cad_original[i]=='i':
            nueva+='pi'
    print(nueva)

cad_original='Hola Mundo'
modif_cadena(cad_original)