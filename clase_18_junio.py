#Clase martes 18 de junio

## NUMEROS ENTEROS = INT O LONG (SIN DECIMALES, PUEDEN SER POSITIVOS, NEGATIVOS O 0)
##LONG 46854854L


## NUMEROS FLOTANTES FLOAT = NUMEROS CON DECIMAL
## EJ: O,35
# -33,895

##NUMEROS COMPLEJOS O COMPLEX = EXTENSION DE NUMEROS REALES
## 33,8j 


# SUMA +
# RESTA -
# MULTIPLICACIÓN *
# POTENCIA **
# DIVISIÓN /
# PROMEDIO %

# PROCEDENCIA DE LOS OPERADORES:
#1 - TERMINOS ENTRE PARENTESIS
#2 - POTENCIACION Y RAICES
#3 - MULTIPLICACION Y DIVISION
#4 - SUMA Y RESTA

""" print(15*8) """

print('hola \t tabulacion')
print('hola \n salto de linea') 


#___VARIABLES___
#LAS VARIABLES EN PY SON COMO ETIQUETAS QUE NOS PERMITEN HACER REFERENCIA A  LOS DATOS.
# POR CADA DATO QUE APARECE EN UN PROGRAMA, PY VA A CREAR UN OBJETO QUE LO CONTIENE
#CADA OBJETO VA A TENER:
#1- UN INDENTIFICADOR UNICO (id)
#2- UN TIPO DE DATO (entero, decimal, string, etc)
#3- UN VALOR (el propio dato adentro)
# LAS VARIABLES EN PY NO GUARDAN DATOS.

dni = 43403426

a = 2

print (dni)


# definir una varieble: a=2

mi_variable = 1974

print (mi_variable)

## EL NOMBRE DE UNA VARIABLE SIEMPRE DEBE EMPEZAR POR UNA LETRA O UN _, PUEDE CONTENER N L Y _ snake_case
## LAS VARIABLES NO PUEDEN INCLUIR ESPACIOS


#METODO DE SALIDA = PRINT()

#METODO DE ENTRADA = INPUT()

nombre = input('Hola, escribí tu nombre!')

print(nombre)

#LA FUNCION INPUT CONVIERTE EL METODO DE ENTRADA EN UN STRING

a = 20
b = 30

resultado = a+b

print(resultado)

c = 100
d = 200

print(c+d)

# LOS DATOS DE ENTRADA SE PODRIAN CONVERTIR DE STR (STRING)

e = 30
""" f = input("Cual es tu edad?") """ # este es un ejemplo de un dato de entrada que lo toma como cadena de texto
""" f = int(input("Cual es tu edad")) """ # CONVERSION DE TIPO: De esta forma logramos que python convierta el STR de entrada en un NUMERO



""" print(e*f) """


cadena_de_texto = "Python SOS LO MEJOR DE MI VIDA TKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM YO"
anio_del_curso = "2024"

print(cadena_de_texto + anio_del_curso)

#A LAS SUMA DE LOS STRINGS LO VAMOS A LLAMAR CONCATENACIÓN

# LOS INDICES VIENEN: 0 (primer caracter), 1 (segundo caracter), etc..
# LOS INDICES INVERSOS: -1(ultimo caracter), -2 (penultimo), etc.. 
# P   Y  T  H  O  N
# 0   1  2  3  4  5 indices
# -6 -5 -4 -3 -2 -1 indice inverso
print(cadena_de_texto[-1])

