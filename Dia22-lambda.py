#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 22 Funciones lambda
#Las funciones lambda son funciones pequeñas y anónimas que no tienen nombre.
#Puden tomar cualquier cantidad de argumentos pero sólo pueden tener una expresión.
#Para quellos que conocen javascript allí se les llaman funciones anónimas
#Y son utilizadas para crear funciones anónimas dentro de otras funciones

#Son útiles cuando:
#Necesitas una función para un tema específico y ya
#Necesitas una función descartable (uso una vez)
#Cuando queremos pasar una función como argumento a una función de orden alto*

# print("Crear una función lambda")
# #Para crear uan función lambda usamos la palabra clave lambda
# #Seguida por los parámetros que requerirá
# #Seguida de una expresión
# print("Sintaxis de la función lambda")
# print("""x = lambda param1, param2, param3: param1 + param2 + param3
# print(x(arg1, arg2, arg3)""")

# print("\nEjemplo 1 Modo tradicional")
# def sumarDos(a, b):
#     return a + b
# print(sumarDos(10,20))

# print("\nEjemplo 2 Modo lambda")
# sumarDos = lambda param1, param2: param1 + param2
# print(sumarDos(10,20))



# print("\nAuto invocar una función lambda")
# #autoinvocar es que la puedo crear y ejecutar sin necesidad de llamarla como una función tradicional
# print((lambda a, b: a + b)(10,20))

# print("\nEjemplo 1")
# #Retorba la potencia 2 de un número
# print((lambda x: x **2)(10))

# print("\nEjemplo 2")
# #Retorba la potencia 3 de un número
# print((lambda x: x **3)(10))



# print("\nLambda con variables múltiples")
# #podemos usar los parámetros que queramos al crear funciones lambda
# print((lambda a,b,c: a**10 - 3 * b + 4 * c)(1,2,3))



# print("\nLambda dentro de funciones")
# def potencia(x):
#     return lambda n : x ** n
# #Necesita el argumento de la función definida + la variable que pide lambda en paréntesis separados

# print("\n Ejemplo 1 Potencia 2")
# cubo = potencia(2)(3)
# print(cubo)

# print("\n Ejemplo 1 Potencia 5")
# potenciaCinco = potencia(2)(5)
# print(potenciaCinco)
