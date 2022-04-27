#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 14 - Bucles
#En programación es común tener que programar actividades repetitivas
#Para ello los lenguajes de programación cuentas con algo llamado "loops" o bucles
#Y en python tenemos dos tipos de bucles ("loops") llamados: while y for

# print("Bucle while")
# #Utilizamos la palabra reservada while para hacer bucles while. Éste es usado
# #Para ejecutar declaraciones o bloques de código repetidamente hasta que se cumpla
# #Una condición, cuando la condición deje de cumplirse se siguen ejecutando lso bloques
# #Siguientes fuera del while loop

# print("\n Sintaxis")
# print("""while condición verdadera:
#             Se ejecuta éste bloque de código 1""")

# print("\n Ejemplo 1")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador = contador + 1 

# print("\n while + condicional")
# #podemos complementar el while con el condicional else para se ejecute un bloque
# #de codigo adicional cuando termine de ejecutarse el while

# print("\n Ejemplo 2")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador = contador + 1
# else:
#     print("Bucle while finalizado")


# print("\n while + break")
# #podemos usar la palabra reservada break para interrumbir el bucle en algún momento

# print("\n Ejemplo 3")
# contador = 0
# while contador < 10:
#     print(contador)
#     contador = contador + 1
#     if contador == 7: #Le digo que cuando llegue a 7 finalice el bucle
#         break
# else: 
#     print("bucle finalizado") #NO se ejecuta el bucle se interrumpió


# print("\n while + continue")
# #Podemos usar la plabra clave continue para saltar a la siguiente parte
# print("\n Ejemplo 4")
# contador = 0
# while contador < 10:
#     print(contador)
#     contador = contador + 1
#     if contador == 7: #Le digo que cuando llegue a 7 salte al a siguiente parte
#         continue
# else: 
#     print("bucle finalizado") #SE ejecuta el bucle poreu saltó acá

# #Ya son unos expertos en el bucle while ahora nos falta el bucle FOR