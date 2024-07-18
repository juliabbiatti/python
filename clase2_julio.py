print ('test')


#___OPERADORES 

# operando [operador] Operando
# operador aritmético (+, -, *, /)
# expresiones aritméticas 2+2 4*3
# expresiones algebraicas: radio * 3.14 (nota1 + nota2)

# Tipo logico BOOLEANO o binario
# Es el tipo de dato más básico de la información racional y representa VERDADERO y FALSO


# Negación
# NO VERDADERO = FALSO
# NO FALSO = VERDADERO 

print (1+1==3)

# operador relacionales son simbolos que se utilizan para comparar dos valores. Si el resultado de la operación es correcto, la expresión nos dará TRUE, sino false.

# OPERADOR DE IGUALDAD (==)
# El operador de IGUALDAD sirve para preguntar si dos valores son iguales. FALSE si no son iguales, TRUE si son iguales. Se escribe (==)

a = 3

print(a == 3)

print(a != 3)

#TRUE == 1
#FALSE == 0

# INICIO - INTERACCION 1 - INTERACCION 2 - INTERACCION 3 - FIN

# SENTENCIA DE CONTROL
# DOS TIPOS =  CONTROL CONDICIONAL Y CONTROL ITERATIVO

#LAS SENTENCIAS DE CONTROL DE FLUJO CONDICIONALES SE VANA  DEFINIR POR EL USO DE TRES PALABRAS CLAVES RESERVADAS:
#if, elif y else
# IF: SI
# ELIF: SINO, SI
# ELSE: SINO

#SENTENCIA IF:
# NOS PERMITE CONTROLAR EL FLUJO DE UN PROGRAMA Y DIVIDIR LA EJECUCIÓN DEL MISMO EN DIFERENTES CAMINOS.
# AL UTILIZAR ESTA PALABARA RESERVADA LE VAMOS A DECIR A PYTHON QUE QUEREMOS EJECUTAR UN BLOQUE DE CODIGO SOLO SI SE CUMPLE DETERMINADA CONDICION, ES DECIR, SI EL RESULTADO ES TRUE.


edad= int(input("Que edad tenés?"))
if edad >= 18:
    print("Sos adulto")

if False:
    print("IMPRIMIME LA CONDICION VERDADERA")