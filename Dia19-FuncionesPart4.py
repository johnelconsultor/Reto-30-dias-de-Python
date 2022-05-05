#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 19 Funciones PARTE 4 Final
#Una función es un bloque reutilizable de código o de declaraciones de programación
#Diseñadas para realizar cierta tarea específica. Para declarar una función
#Utilizaremos la palabra clave def. Hay que recordar que el bloque de código
#De una función sólo será ejecutado SOLAMENTE si la función es llamada

# print("Declarando una función con parámetros por default")
# #Cuando creamos una función lo llamamamos "declarar" una función y cuando
# #comenzamos a usarla a ésto se le dice "llamar" o "invocar".
# #Una función puede ser declarada con o sin parámetros

# print("\nSintaxis de una función con parámetros por default")
# print("""def nombreDeLaFuncion ( parametro1 = valorDefault1 ):
#             bloque de código a ejecutar""")

# print("\nEjemplo 1")
# def saludo (nombre = "Dataadict@"):
#     mensaje = nombre + " Que guapo eres bby ;)"
#     return mensaje

# print(saludo())
# print(saludo("John"))

# print("\nEjemplo 2")
# def pesoObjeto (masa, gravedad = 9.81):
#     peso = str( masa * gravedad) + " N"
#     return peso

# print(pesoObjeto(10,)) #Peso en la tierra
# print(pesoObjeto(10, 1.62)) #Gravedad en la luna = Peso en la luna

# print("\n Declarando una función con una cantidad de parámetros desconocidos")
# #Si no conocmeos el número de argumentos que pasaremos en una función, podemos
# #Crear una función que pueda recibir una cantidad indeterminada de argumentos
# #Añadiendo * antes del nombre del parámetro
# def sumarTodos(*numeros):
#     total = 0
#     for i in numeros:
#         total += i
#     return total

# print(sumarTodos(1,2,3,4))

# print("\n Declarando una función con parámetros default y cantidad desconocida")
# #Podemos crear funciones que combinen todo lo que hemos visto parámetros default
# #y parámetros con uan cantidad desconocida de argumentos
# def generarGrupo (numGrupo, *integrantes):
#     personasEnGrupo = []
#     for i in integrantes:
#         personasEnGrupo.append(i)
#     grupo = f" El # del Grupo es{numGrupo} y los integrantes {personasEnGrupo}"
#     return grupo

# print(generarGrupo(10,"pedro","juan","john"))


# print("\nUna función como parámetro de otra función")
# #Las funciones pueden alimentar a otras funciones fungiendo como argumento
# def numeroCuadrado(numero):
#     return numero * numero

# def sumaNumero(x, y):
#     return x + y

# print(sumaNumero(numeroCuadrado(10),23))


# #Mis queridos dataadictos y dataadictas si vieron los 4 tiktokds sobre funciones
# #Ya son todos unos expertos