#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 19 Funciones PARTE 3
#Una función es un bloque reutilizable de código o de declaraciones de programación
#Diseñadas para realizar cierta tarea específica. Para declarar una función
#Utilizaremos la palabra clave def. Hay que recordar que el bloque de código
#De una función sólo será ejecutado SOLAMENTE si la función es llamada


print("\La función devolviendo un valor")
#En tiktoks anteriores vimos como necesitamos la palabra clave return
#Para que la función devuelva un valor y que en caso de no usarla la función
#devuelve como resultado None por default. Debemos tener presente que las 
#Funciones puden devolver cualquier tipo de dato

print("\n Devolviendo un string")
def saludo (nombre):
    mensajeSaludo = f"hola {nombre} eres una guapura!"
    return mensajeSaludo

print(saludo("john"))
print(type(saludo("john")))


print("\n Devolviendo un int")
def sumaDosNumeros (parametro1, parametro2):
    total = parametro1 + parametro2
    return total

print(sumaDosNumeros(10, 25))
print(type(sumaDosNumeros(10, 25)))


print("\n Devolviendo un float")
def division(dividendo, divisor):
    resultado = dividendo / divisor
    return resultado

print(division(5,10))
print(type(division(5,10)))

print("\n Devolviendo un bool")
print()