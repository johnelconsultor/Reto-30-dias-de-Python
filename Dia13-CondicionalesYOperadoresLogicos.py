#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 13 - Condicionales y Operadores lógicos
#Por default las declaraciones en un script the python son ejecutadas de arriba hacia abajo. Si la lógica del proceso requiere que éste flujo sea alterado puede hacerse de dos modos
#1. Ejecución condicional: Un bloque de una o más declaraciones se ejecutarán si una expresión es verdadera
#2. Ejecución repetitiva: Un bloque de una o más declaraciones se ejecutarán repetitivamente siempre y cuando una expresión sea verdadera.
#Para lo anterior utilizaremos los condicionales

#Los condicionales son palabras clave que nos permiten controlar el flujo lógico de un programa resultando la alteración de la secuencialidad de lectura arriba hacia abajo

# print("Condiciones anidadas")
# #Los condicionales pueden ir anidados "uno dentro de otro" todas las veces que queramos para crear flujos complejos en nuestro programa

# print("Sintaxis")
# print("""if condición:
#         esta parte se ejecuta si la condición fue cierta
#         dentro de éstae bloque podemos tener otra condición
#             if nueva condicion:
#                 esta parte se ejecuta si la nueva condición es cierta
#         """)

# print("\n Ejemplo ")

# numero = 10
# if numero > 0:
#     if numero % 2 == 0:
#         print(f"el numero es par, posito y entero")
#     else:
#         print(f"el numero es positivo")
# elif numero == 0:
#     print("El numero es cero")
# else:
#     print("El numero es negativo")


# print("\n Incluyendo Operadores lógicos")
# #Podemos utilizar operadores lógicos para ahorrarnos anidar IF's
# print("If y el operador lógico AND")

# numero = 10
# if numero > 0 and numero % 2 ==0:
#     print("El número es par, postivo y entero")
# elif numero >0 and numero % 2 != 0:
#     print("El numero es positivo")
# elif numero == 0:
#     print("El numero es 0")
# else:
#     print("El numero es negativo")


# print("If y el operador lógico OR")
# #Podemos USAR OR para verificar un criterio entre varias declaraciones. si no saben cómo funciona el AND y el OR se pueden devolver al día 5 donde vimos operadores lógicos

# print("\n Ejemplo 2")
# usuario = "gerente"
# nivelAcceso = 10

# if usuario == "ejecutivo" or nivelAcceso > 5:
#     print("Tiene accceso")
# else:
#     print("No tiene acceso")

# print("\n Escritura corta")
# #Los flujos de lógica pueden ser escritos de una manera lineal para resumir
# usuario = "gerente"
# nivelAcceso = 10

# print("Tiene acceso") if usuario == "ejecutivo" or nivelAcceso > 10 else print("sin acceso")
# #En ésta forma de declarar los flujos lógicos es obligatorio cerrar el if con un else para que python lo agarre

# #Ya son unos expertos en uso de condicionales con operadores lógicos