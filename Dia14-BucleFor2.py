# #JOHN EL CONSULTOR PRESENTA
# #Aprende PYTHON desde el Telefóno
# #En mi perfil de tiktok encuentran:
# #1 Link a mi web donde esta python
# #2 Lista de reproducción con el curso

# #Dia 14 - Bucles
# #En programación es común tener que programar actividades repetitivas
# #Para ello los lenguajes de programación cuentas con algo llamado "loops" o bucles
# #Y en python tenemos dos tipos de bucles ("loops") llamados: while y for

# print("\nFor y la función range")
# #En el tiktok anterior vimos cómo hacer funciona el bucle for usando estructuras de datos
# #ahora veremos cómo hacerlo con la función range

# print("Función range")
# #Permite generar una secuencia de números de manera rápida que puede ser almacenada
# listaNumeros = list(range(0,6)) #Genera números del 1 al 5 (recordar cómo funciona slicing)
# print(listaNumeros) #Con ésta seacuencia yo le puedo decir al for que itere sobre cada item

# print("For y la función range")
# for i in listaNumeros:
#     print(i) #For itera sobre cada item y print lo imprime en pantalla

# print("\n Bucle for y palabras reservadas")
# #Al igual que le bucle while podemos utilizar las palabras reservadas
# #break y continue con éste bucle
# print("Bucle for y break")
# #Recordemos que break lo usamos cuando queremos interrumpir un bucle

# print("Sintaxis")
# print("""for iterador en secuencia:
#     (tab) bloque de código a ejecutar
#     (tab) condicional:
#         palabra clave break para interrumpir""")

# print("\nEjemplo for con break")
# for i in listaNumeros:
#     print(i)
#     if i == 3:
#         break #Interrumpe al llegar a tres el bucle

# print("Bucle for y continue")
# #Recordemos que el continue nos permite saltarnos pasos de la ejecución
# #Con base en un criterio
# print("Sintaxis")
# print("""for iterador en secuencia:
#     (tab) bloque de código a ejecutar
#     (tab) condicional:
#         palabra clave continue para saltar a siguiente""")


# print("\nEjemplo for con continue")
# for i in range(0,11):
#     if i % 2 == 1 or i == 0:
#         continue #Salta la ejecución cuando es impar
#     print(i)


# print("\nEjemplo for con pass")
# #En python necesitamos una declaración siempre que usamos los :
# #En alguna parte. Usamos la palabra reservad pass si quieremos
# #dejar una plantilla para algo y no queremos que hayan errores
# for i in range(0,6):
#     pass


# print("\nfor anidados")
# #Claro que podemos tener bucles dentro de bucles
# #las combinaciones en programación son infinitas
# #Solo tengan mucho cuidado de declarar bien dónde deben
# #Terminar las ejecuciones

# print("Sintaxis")
# print("""for x in y:
#     (tab) for a in b:
#     (tab) (tab) ejecutar éste bloque de código""")

# #Acá tengo un diccionario con mis datos
# persona = {
#     'nombre':'John',
#     'apellido':'Arias',
#     'edad':32,
#     'país':'Colombia',
#     'casado':True,
#     'habilidades':['Excel', 'BI', 'PP', 'PPt', 'Python'],
#     'dirección':{
#         'calle':'Siempre viva 123',
#         'codigozip':'1111111'
#     }
#     }

# print("\n Ejemplo de for dentro de for")
# #Qué creen que hará éste bloque de código?
# for i in persona:
#     if i == "habilidades":
#         for habilidad in persona["habilidades"]:
#             print(habilidad)

# print("\n Ejemplo2 finalizando con mensaje")
# #Qué creen que hará éste bloque de código?
# for i in persona:
#     if i == "habilidades":
#         for habilidad in persona["habilidades"]:
#             print(habilidad)
#         else:
#             print(f"Termino en llave '{i}'") #Para saber en qué llave acabó

# #Mis queridos datadictos y dataadictas ya son unos expertos en el bucle for