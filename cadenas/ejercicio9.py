"""11. Diseñar un programa que permita realizar el registro a una aplicación de estudiantes de una universidad, cada
 estudiante cuenta con los siguientes atributos: dni, clave, nombre, eMail y número de celular. Se solicita
 desarrollar las siguientes funcionalidades:
 a.
 Registrarse en la aplicación: Se solicitan los datos del estudiante con las siguientes validaciones:
 ○ dni: es de tipo string debe tener 8 dígitos numéricos, luego de ingresar este valor se debe verificar que
 no exista actualmente.
 ○ clave: debe tener como mínimo una longitud de 6 caracteres, al menos una mayúscula y un número
 ○ nombre: no puede tener números ni caracteres especiales y al menos 3 caracteres
 ○ eMail: debe verificar que tenga el @ y que no se encuentre al inicio ni al final de la cadena ingresada.
 ○ Número deCelular: debe incluir el código de área más el número sin el 15 (por ejemplo 388-4800123),
 es decir:
 ■ Los primeros dígitos corresponden al código de área y los valores solo pueden ser 388, 3886,
 3887 y 3888
 ■ Elguión es obligatorio
 ■ Losrestantes números corresponden al número de celular y su longitud debe ser de 7 dígitos.
 El registro de estudiantes debe realizarse utilizando una estructura de tipo lista de listas que estará
 inicializada con 10 estudiantes para facilitar las pruebas.
 b. Buscar un estudiante: el programa solicitará el nombre y en función de ello mostrará lo siguiente:
 ● Siseingresa un vacío (enter), el programa mostrará la lista completa de estudiantes registrados
 ● Si se ingresa un nombre, el programa mostrará los estudiantes cuyos nombres contengan al valor
 ingresado, por ejemplo si ingresa ana, mostrará Mariana, Analía, etc.
 c.
 Ingresar (Login): debe solicitar el dni y la clave y verificar que coincida con algún estudiante registrado, si no
 existe emitirá el mensaje “Usuario o Clave incorrectos”. Si los datos son correctos mostrará el mensaje
 “Ingreso exitoso” y también mostrará el nombre y correo electrónico del estudiante"""