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

print("Declarando una función con parámetros por default")
#Cuando creamos una función lo llamamamos "declarar" una función y cuando
#comenzamos a usarla a ésto se le dice "llamar" o "invocar".
#Una función puede ser declarada con o sin parámetros

print("\nSintaxis de una función con parámetros por default")
print("""def nombreDeLaFuncion ( parametro1 = valorDefault1 ):
            bloque de código a ejecutar""")

print("\nEjemplo 1 de función con parámetro por default")
def saludo (nombre = "Dataadict@"):
    mensaje = nombre + " Que guapo eres bby ;)"
    return mensaje

print(saludo())
print(saludo("John"))

print("\nEjemplo 2 de función con parámetro estándar")
def pesoObjeto (masa, gravedad = 9.81):
    peso = str( masa * gravedad) + " N"
    return peso

print(pesoObjeto(10,)) #Peso en la tierra
print(pesoObjeto(10, 1.62)) #Gravedad en la luna = Peso en la luna


