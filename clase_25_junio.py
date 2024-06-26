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

print(listita[0])
print(listita[-1])

print(listita + [otra_lista, 'HOLA']) #CONCATENAR

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros+[11,12,13,14,15,16,17,18,19,20]) #LAS LISTAS SON MUTABLES

numeritos = [0, 2, 4, 5]
numeritos[0] = 5 #REASIGNAR VALOR, LAS LISTAS SON MUTABLES (NO ASÍ LOS STRINGS)
print(numeritos)

#FUNCION APPEND, NOS PERMITE AGREGAR UN NUEVO ITEM AL FINAL DE LA LISTA

numerillos = [1, 2, 3, 4, 5]
numerillos.append(999)
print(numerillos)

numerillos = [1, 2, 3, 4, 5]
numerillos.append(9*2) #LO MISMO CON CALCULOS
print(numerillos)

print(len(numerillos)) #contabiliza items

#Funcion POP
#Es lo contrario a APPEND, elimina el ultimo item

'''equipos = ['River', 'Boca', 'Velez', 'Racing']
equipos.pop()
print(equipos) #ELIMINA A RACING'''

equipos = [1, 2, 3, 4]
equipos.pop(2) #ELIMINA EL ITEM QUE ESTA EN ESA POSICIÓN
print(equipos) 

#FUNCION COUNT

numeros_varios = [1, 2, 3, 4, 5, 5, 4, 5]
numeros_varios.count(5) #cuantas veces aparece el 5? devuelve 3
print(numeros_varios.count(5))

#FUNCION INDEX busca el item y nos dice en que índice está


numeros_variados = [1, 2, 3, 4, 5, 5, 4, 5]
numeros_variados.index(2) #en que posicion de la lista está el número 2? (en el 1)
print(numeros_variados.index(2))


#TUPLAS Colecciones de datos parecidas a las listas, son inmutables, a los arrays podiamos reasignarlos, a las tuplas no. Se utiliza para asegurarnos que los datos no se puedan modificar y evitar errores en el código. En vez de corchete se utiliza paréntesis.

mi_tupla = (1, 2, 3)
print(mi_tupla[0])

#LAS FUNCIONES FUNCIONAN IGUAL QUE CON LOS ARRAYS, PERO CON PARENTESIS Y EL INDICE BUSCADO EN CORCHETE, pero no puede modificarse y reemplazarse los datos como con el array, ej no funciona el append, si se puede utilizar count, index, len, buscar el item

