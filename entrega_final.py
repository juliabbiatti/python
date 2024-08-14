# Ejercicio 1: Números y Cadenas de Caracteres

# 1.Escribe un programa que pida al usuario dos números enteros y realice lo siguiente:

num1 = int(input("Introduzca un número entero: "))
num2 = int(input("Introduzca un segundo número entero: "))

# Muestra la suma de los dos números.
print("Suma:", num1 + num2)

# Muestra el producto de los dos números.
print("Producto:", num1 * num2)

# Muestra la concatenación de los dos números (como texto).
print("Concatenación:", str(num1) + str(num2))

# 2.Pide al usuario una cadena de texto. Luego muestra:

cadena = input("Introduzca una cadena de texto: ")

# La cadena en mayúsculas.
print("Mayúsculas:", cadena.upper())

# La longitud de la cadena.
print("Longitud:", len(cadena))

# La cadena invertida.
print("Invertida:", cadena[::-1])

# La cantidad de veces que aparece una letra específica (elige una letra y pídesela al usuario).
letra = input("Introduzca una letra: ")
print("Cantidad de veces que aparece la letra: ", cadena.count(letra))

# 3.Escribe un programa que convierta un número decimal a binario y viceversa.
numero_decimal = float(input("Introduce un número decimal: "))
numero_binario = input("Introduzca un número binario: ")
print("Decimal:", int(numero_binario, 2))
print("Binario (solo parte entera):", bin(int(numero_decimal))[2:])
numero_binario = input("Introduce un número binario: ")
print("Decimal:", int(numero_binario, 2))


# 4.Pide al usuario una cadena y un número entero. Muestra la cadena repetida el número de veces indicado por el número entero.
cadena_repetir = input("Introduzca una cadena: ")
num_repetir = int(input("Introduzca un número entero: "))
print("Cadena repetida: ", cadena_repetir * num_repetir)



# Ejercicio 2: Listas y Tuplas.
# Crea una lista con los nombres de tres frutas. Luego:

# Creamos una lista con nombres de tres frutas
frutas = ["banana", "sandia", "melon"]

# Añade dos frutas más a la lista.
frutas.append("pera")
frutas.append("mandarina")

# Ordena la lista alfabéticamente.
frutas.sort()

# Muestra la lista completa.
print("Lista de frutas:", frutas)

# Elimina una fruta de la lista y muestra el resultado.
frutas.remove("banana")
print("Lista después de eliminar una fruta: ", frutas)

# 2.Crea una tupla con los nombres de dos ciudades. Luego:
ciudades = ("CABA", "Córdoba")

# Muestra el primer y último elemento de la tupla.
print("Primera ciudad:", ciudades[0])
print("Última ciudad:", ciudades[-1])

# Convierte la tupla en una lista, añade una nueva ciudad y muestra la lista resultante.

lista_ciudades = list(ciudades)
lista_ciudades.append("Rosario")
print("Lista de ciudades:", lista_ciudades)

# 3.Crea una lista de números enteros y muestra:
numeros = [1, 2, 3, 4, 5]

#El número mayor de la lista.
print("Número mayor:", max(numeros))
#El número menor de la lista.
print("Número menor:", min(numeros))
#El promedio de los números en la lista.
print("Promedio:", sum(numeros)/len(numeros))

# 4. Escribe un programa que reciba una lista de cadenas y muestre la lista con todas las cadenas en mayúsculas.
cadenas = ["hola", "como", "estas"]
cadenas_mayus = [cadena.upper() for cadena in cadenas]
print("Cadenas en mayúsculas:", cadenas_mayus)

# Ejercicio 3: Controladores de Flujo

# 1.Escribe un programa que pida un número al usuario. Muestra si el número es par o impar.

numero = int(input("Introduzca un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# 2.Crea un programa que simule un menú simple con las siguientes opciones
opcion = 0
while opcion != 3:  
    print("Menú:")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    
    try:
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            print("Hola")  
        elif opcion == 2:
            print("Chau")  
        elif opcion == 3:
            print("Saliendo")  
        else:
            print("Opción no válida")  

    except ValueError:
        print("Ingrese un número válido.")

# 3.Escribe un programa que pida un número al usuario y determine si es positivo, negativo o cero.
numero = int(input("Introduzca un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# 4. Escribe un programa que muestre los números del 1 al 10 utilizando un bucle for.
for i in range(1, 11):
    print(i)

# 5. Escribe un programa que calcule la suma de los números del 1 al 100 utilizando un bucle while.
suma = 0
i = 1
while i <= 100:
    suma += i
    i += 1
print("Suma del 1 al 100:", suma)

# Ejercicio 4: Conjuntos y Diccionarios

# 1.Crea dos conjuntos con algunos números. Luego:
conjunto1 = {1, 6, 8, 2, 3}
conjunto2 = {6, 4, 8, 9, 2}

# Muestra la unión de los dos conjuntos.
print("Unión conjuntos:", conjunto1 | conjunto2)

# Muestra la diferencia entre los dos conjuntos.
print("Diferencia conjuntos:", conjunto1 - conjunto2)

# Muestra los elementos comunes en ambos conjuntos.
print("Elementos comunes:", conjunto1 & conjunto2)

#2.Crea un diccionario con tres nombres como claves y edades como valores. Luego:
edades = {"Julieta": 23, "Joaquin": 25, "Sol": 24}

# Muestra la edad del primer nombre en el diccionario.
print("Edad de Julieta:", edades["Julieta"])

# Añade un nuevo nombre y edad al diccionario.
edades["Estefanía"] = 33

# Elimina un nombre del diccionario y muestra el resultado.
del edades["Sol"]
print("Diccionario con un nombre menos:", edades)

# Muestra todas las claves y todos los valores del diccionario.
print("Claves del diccionario:", edades.keys())
print("Valores del diccionario:", edades.values())

# Crea un diccionario con los nombres de cinco productos como claves y sus precios como valores. Luego:
productos = {"Leche": 2000, "Harina": 1500, "Aceite": 2500, "Yogurt": 1000, "Yerba": 2500}

# Muestra el precio de un producto específico.
print("Precio de la yerba:", productos["Yerba"])

# Incrementa el precio de todos los productos en un 10%.
# Muestra el diccionario actualizado.
productos_actualizados = {producto: precio * 1.10 for producto, precio in productos.items()}
print("Diccionario con los precios actualizados:", productos_actualizados)

# Crea un conjunto con los números del 1 al 5 y otro conjunto con los números del 4 al 8. Muestra:

conjunto3 = {1, 2, 3, 4, 5}
conjunto4 = {4, 5, 6, 7, 8}

# La intersección de los dos conjuntos.
print("Intersección de conjuntos:", conjunto3 & conjunto4)

# La diferencia simétrica entre los dos conjuntos.
print("Diferencia simétrica:", conjunto3 ^ conjunto4)

# Ejercicio 5: Funciones

# Define una función saludar(nombre) que reciba un nombre y muestre un saludo. Luego llama a esta función con tu propio nombre.
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Julieta")

# Define una función suma(a, b) que reciba dos números y retorne su suma. Luego prueba la función con dos números diferentes.
def suma(a, b):
    return a + b

print("Suma de 1 y 4:", suma(1, 4))

# Define una función es_mayor_de_edad(edad) que reciba una edad y retorne True si la edad es mayor o igual a 18 y False en caso contrario. Prueba la función con diferentes edades.

def es_mayor_de_edad(edad):
    return edad >= 18

print("Es mayor de edad (15):", es_mayor_de_edad(15))
print("Es mayor de edad (40):", es_mayor_de_edad(40))
