# #JOHN EL CONSULTOR PRESENTA
# #Aprende PYTHON desde el Telefóno
# #En mi perfil de tiktok encuentran:
# #1 Link a mi web donde esta python
# #2 Lista de reproducción con el curso

# #Dia 14 - Bucles
# #En programación es común tener que programar actividades repetitivas
# #Para ello los lenguajes de programación cuentas con algo llamado "loops" o bucles
# #Y en python tenemos dos tipos de bucles ("loops") llamados: while y for

# print("Bucle for")
# #Utilizamos la palabra reservada for para hacer bucles for. A diferencia
# #A diferencia del bucle while el bucle for se utiliza normalmente
# #Para iterar sobre una secuencia(listas, tuplas, dicts, sets, str..)
# #O rangos definidos de números

# print("Sintaxis")
# #El mejor modo de entenderlo es verlo cómo una forma de repetir un bloque
# #de código por una cantidad de veces definida a través de una secuencia
# #o rango de números
# print("""for (iterador) in lista/dict/string/set... o rango de números:
#             (tab o espacios) El bloque de código que queremos se repita """)

# print("\nEjemplo 1: For con una lista")
# for items in [1,2,3]: #items respresenta c/d objeto en la list
#     print("Hola Dataadicto")

# print("\nEjemplo 2: For con una lista")
# for letras in "john": #letras respresenta c/d carácter en el str
#     print("Hola Dataadicto 2.0")

# print("\nEjemplo 3: For con una tupla")
# for num in (1,2,3): #num respresenta c/d objeto en la tupla
#     print("Hola Dataadicto 3.0")

# print("\nEjemplo 4: For con un diccionario")
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

# print("For para sacar llaves")
# #Podemos usar el bucle for para sacar las llaves de un diccionario
# for llaves in persona: #Llaves respresenta c/d objeto en el dic
#     print(llaves)

# print("\nFor y .items() para sacar llaves")
# #Podemos ayudarnos del método .items() para decirle a python que queremos
# #iterar sobre los objetos de un diccionario y sacar las llaves, valores o ambos
# for llaves, valores in persona.items(): #Llaves respresenta c/d objeto en el dic
#     print(llaves)

# print("\nFor para sacar valores")
# #Podemos usar el bucle for para sacar las llaves de un diccionario
# for llaves, valores in persona.items(): #Llaves respresenta c/d objeto en el dic
#     print(valores)

# print("\nFor para sacar Llaves y valores")
# #Podemos usar el bucle for para sacar las llaves y valores de un diccionario
# for k, v in persona.items():
#     print(k, v)

# #Ya aprendimos lo básico de los bucles for pero aún nos falta un poco para
# #dominarlo, nos vemos en el siguiente tiktok donde hablaremos más  sobre
# #el bucle for