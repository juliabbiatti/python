#DESTINADO A LAS TAREAS


#CLASE 18/6: CREAR UN SCRIPT EN EL QUE PODAMOS CALCULAR LA NOTA FINAL EN BASE A 5 EXAMENES, ESTOS EXAMENES EQUIVALEN A UN PORCENTAJE DE LA NOTA FINAL.

# LA NOTA NUMERO 1 CORRESPONDE AL 20% DE LA NOTA FINAL.
# LA NOTA NUMERO 2 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 3 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 4 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 5 CORRESPONDE AL 50% DE LA NOTA FINAL.

#A esto se lo suele llamar promedio ponderado: no todos los valores tienen el mismo "peso".
#Por ejemplo, dado el ejercicio de arriba me conviene sacarme una mejor nota en el examen donde la nota vale casi el 50% de la nota final.

# Solicitar las notas de los exámenes al usuario
'''nota1 = float(input("Ingrese la nota del examen 1 (20%): "))
nota2 = float(input("Ingrese la nota del examen 2 (10%): "))
nota3 = float(input("Ingrese la nota del examen 3 (10%): "))
nota4 = float(input("Ingrese la nota del examen 4 (10%): "))
nota5 = float(input("Ingrese la nota del examen 5 (50%): "))

# Porcentajes asignados a cada examen
porcentaje1 = 0.20
porcentaje2 = 0.10
porcentaje3 = 0.10
porcentaje4 = 0.10
porcentaje5 = 0.50

# Calcular la nota final
nota_final = (nota1 * porcentaje1) + (nota2 * porcentaje2) + (nota3 * porcentaje3) + (nota4 * porcentaje4) + (nota5 * porcentaje5)'''

# Mostrar la nota final
###print("La nota final es: " + str(nota_final))



#CLASE 25/6: TENIENDO DOS LISTA LA CUAL LLAMAREMOS lista_1 y lista_2 hay que hacer los siguientes ejercicios

lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = [7, 8, 9, 10, 11, 12]
#Añadir a la lista_1 el entero 4567 y despues el string "UNAHUR"
lista_1.append(4567)
print(lista_1 + ["UNAHUR"])

#Añadir a la lista_2 el string "EDUCACION" y despues el entero 789

lista_2.append('EDUCACION')
lista_2.append(789)
print(lista_2)

#Crear una lista_3 con todos los elementos de la lista_1 MENOS el último

lista_3 = lista_1
print(len(lista_1))
print(lista_1)
lista_3.pop(6)
print(lista_3)

#Crear una lista_4 con todos los elementos de la lista_2 MENOS el primero y último

lista_4 = lista_2[1:-1]
print(lista_4)

#Crear una lista_5 con todos los elementos de la lista_3 y de la lista_4

lista_5 = lista_3 + lista_4
print(lista_5)

#                              AHORA CON TUPLAS
#Crear una variable llamada tupla con más de 15 items y printear lo siguiente:

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)


# El ultimo item de la tupla creada, el numero de items de la misma, la posicion donde se encuentra algun item que haya dentro, una lista con los ultimos cuatro items de la tupla, un item que haya en la posicion 8, el numero de veces que se repite algún item dentro de la misma.

print(tupla[-1]) #El último ítem de la tupla
print(len(tupla)) #El número de ítems
print(tupla.index(5)) #La posición de alguno de los ítem
print(list(tupla[-4:])) #Los últimos 4 ítem de la lista
print(tupla.index(8)) #Ítem en la posición 8
print(tupla.count(3)) #El número de veces que el número 3 se repite



#CLASE 16 de Julio, analizar el código y explicar que hace cada linea, luego reemplazarlo por otra condición
#WHILE

n = 10 #La condición es 10
while n<10: #Mientras la condición sea menor a 10
    if (n%2)==0: 
        print(n,"Es un numero par") #Imprimir es un número par si el residuo de la división de la constante por dos es 0
    else:
        print(n,"es un numero impar")  #Si el residuo no da 0, imprimir es un numero impar
    n+=1 #Iteración incrementar de a 1
#En este caso no ocurriría el bucle porque n es igual a 10, y el requisito para que esto ocurra es que sea menor a 10.

n = 9 #En este caso sí nos da el resultado.
while n<10:
    if (n%2)==0:
        print(n,"Es un numero par")
    else:
        print(n,"es un numero impar")
    n+=1
    



#  IF ELSE ELIF
# Construir un algoritmo con lo viste en clase bajo el mismo diagrama de flujo de la imagen que está en la carpeta assets del repo


def inicio(selecciona):
    if selecciona == "entrar":
        print("Bienvenido al sistema")
    elif selecciona == "saludo":
        print("Hola! ¿Cómo estás?")
    elif selecciona == "salir":
        print("Saliendo del sistema")
    else:
        print("No se reconoce el comando")
    
inicio("entrar")
inicio("saludo")
inicio("salir")
inicio("otra cosa")

# SETS
# Es una variable grupo:
#Añadir a las siguientes personas: Jose, Maria, Gerardo, Fabian
#Eliminar a las personas: Fernando, Federico, Francisco

grupo = {"Fernando", "Federico", "Francisco", "Ricardo"}

grupo.update({"Jose", "Maria", "Gerardo", "Fabian"})

grupo.difference_update({"Fernando", "Federico", "Francisco"})

print(grupo)


# DICCIONARIOS
animalitos = {"elefante": ""}
# Añadir al diccionario las claves perro, gato y tucan con sus valores "Tobi", "Michi" y "Diego"
animalitos.update({"perro": "Tobi", "gato": "Michi", "tucan": "Diego"})


# Modificar la clave elefante por delfin
animalitos["delfin"] = animalitos.pop("elefante")

print(animalitos)