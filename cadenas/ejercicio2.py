""" 4. Ingresar una dirección de email por teclado. Verificar que la cadena ingresada contiene un solo caracter @ """

email=str(input('Ingrese email: '))
while email.count('@')>1 or email.count('@')==0:
    print('Email invalido')
    email=str(input('Ingrese email valido: '))
print('Bienvenido')