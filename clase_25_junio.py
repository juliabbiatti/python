#LONGITUD DE STR
#LEN (CONTAR CARACTERES)

un_string = 'Hola'

print(len(un_string))

#REBANAR UN STRING
#Función SLICING [inicio:fin:paso]
#Inicio es el índice del primer caracter de la cadena que queremos rebanar.
#Fin el ultimo caracter de la cadena no incluido que queremos rebanar.
#Paso es cada cuanto caracteres seleccionamos entre las posiciones de inicio y fin.

saludo = 'Hola, como están?'
print(len(saludo))
saludo[0:3:1]
print(saludo[0:17:2])

palabra = 'Pithon'
print(palabra)

print(palabra[1])

palabra = palabra[0:1] + 'y' + palabra [2:] #para reemplazar la i por la y, agarro solo la p, le agrego la 'y' y despues el thon. Las cadenas de texto son inmutables, por eso se busca la forma. Esto es SLICING, se toma un parte de la palabra, se suma una letra y se suma la otra parte de la palabra.
print(palabra)

#Lista y Tuplas

mi_lista = [-11, 20, 3, 41]
print(mi_lista)

otra_lista = ['Hola', 'como', 'están', '?']

variable_1 = 'Una variable'

listita = [1, -10, 135.2, 'un string', variable_1]
print(listita)