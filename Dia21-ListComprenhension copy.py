#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 21 List Comprehension
#List comprehension en Python es un modo compacto de crear una lista de una secuencia.
#Es una manera corta de crear una nueva lista. List comprenhension es más rápido
# qeu procesar un foor loop del modo tradicional

# print("Ejemplo 1 Strings a listas")
# #Si queremos cambiar un string a una lista se pueden usar diferentes modos
# print("Modo 1 funcion list()")
# #Modo tradicional usando la función lista
# nombre = 'John el Consultor'
# lista = list(nombre)
# print(type(lista))
# print(lista)       

# print("Modo 2 list comprenhension")
# #Utilizando el list comprenhension
# lista = [i for i in nombre]
# print(type(lista))
# print(lista)



# print("\nEjemplo 2 Generando listas de numeros")
# #Podemos generar listados de números también

# print("Modo 1 list comprenhension + range")
# numeros = [i for i in range(11)]
# print(numeros)

# print("Modo 2 list comprenhension + operaciones")
# numeros = [i * i for i in range(11)] #Multiplica cada núm por si mismo
# print(numeros)

# print("Modo 3 list comprenhension + hacer tuplas")
# numeros = [(i, i * i) for i in range(11)]
# print(numeros)



# print("\nEjemplo 3 combinando con condicionales")
# #Podemos combinar list comprenhension con condicionales

# print("Modo 1 Crear una lista de pares")
# pares = [i for i in range(11) if i % 2 == 0]
# print(pares)

# print("Modo 2 Crear una lista de impares")
# impares = [i for i in range(11) if i % 2 != 0]
# print(impares)

# print("Modo 3 para filtrar números")
# enteros = list(range(-10,11))
# enterosPares = [i for i in enteros if i % 2 == 0 and i > 0]
# print(enterosPares)

