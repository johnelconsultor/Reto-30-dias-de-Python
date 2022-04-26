#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 13 - Condicionales
#Por default las declaraciones en un script the python son ejecutadas de arriba hacia abajo. Si la lógica del proceso requiere que éste flujo sea alterado puede hacerse de dos modos
#1. Ejecución condicional: Un bloque de una o más declaraciones se ejecutarán si una expresión es verdadera
#2. Ejecución repetitiva: Un bloque de una o más declaraciones se ejecutarán repetitivamente siempre y cuando una expresión sea verdadera.
#Para lo anterior utilizaremos los condicionales

#Los condicioanales son palabras clave que nos permiten controlar el flujo lógico de un programa resultando la alteración de la secuencialidad de lectura arriba hacia abajo

print("\Condicional: If")
#Traduce al español "si" y el mejor modo de entenderlo es "si" ésto se cumple "has" ésto otro
#La palabra clave para usarlo es if y es usado para verificar si una condición es falsa o verdadera y para ejecutar un bloque de código acorde a esa condición.
#SIEMPRE DESPUÉS DE IF DEBE HABER INDENTACIÓN(ESPACIO) CONVENCIÓN: 1 TAB o 5 ESPACIOS

print("Sintaxis")
print("""if condición:
         esta parte se ejecuta si la condición fue cierta""")

#Ejemplo
if True:
    print("\n Hola data adictos")

if False:
    print("No sale nada, condición no se cumple")

#¿Cuál va a ser el resultado del siguiente?
numero = 5
resultado = ""
if numero > 10:
    resultado = f"El {numero} es mayor que 10"
if numero < 15:
    resultado = f"El {numero} es menor que 10" 
print(resultado)


print("\n Condicional: Else")
#Traduce "si además" y nos sirve para poner una condición que se ejecutará cuando todas las condiciones anteriores son falsas
#El mejor modo de entenderla es si ninguna de las otras es... entonces ésto
print("Sintaxis")
print("""if condición:
        esta parte se ejecuta si la condición fue cierta

        else:
        Si la condición anterior o condiciones anteriores son falsas se ejecuta""")

#Ejemplo
if False:
    print("No sale nada, condición no se cumple")
else:
    print("\n Si la anterior fue falsa sale ésta")

#¿Cuál va a ser el resultado del siguiente?
resultado = "o" in "john"
if resultado:
    print("\n Se ejecuta éste bloque 1")
else:
    print("\n Se ejecuta éste bloque 2")


print("\n Condicional: elif")
#Utilizamos elif para cuando tenemos diferentes opciones de las cuales escoger
#El mejor modo de entenderla es si la anterior no cumple revisa la siguiente y así sucesivamente
print("Sintaxis")
print("""if condición:
        esta parte se ejecuta si la condición fue cierta

        elif condición2:
        si la anterior es falsa revisa ésta otra condición

        elif condición3:
        si la anterior es falsa revisa ésta otra condición

        else:
        si ya nada de lo anterior se cumplió pon ésto y acá termina""")

#De acuerdo a todo lo anterior previo a ejecutar pensemos cuál se ejecutará
print("\n Ejemplo 1")
if True:
    print("Se ejecuta ésta condición 1")
elif False:
    print("Se ejecuta ésta condición 2")
elif False:
    print("Se ejecuta ésta condición 3")
else:
    print("Se ejecuta ésta condición 4")

print("\n Ejemplo 2")
if False:
    print("Se ejecuta ésta condición 1")
elif True:
    print("Se ejecuta ésta condición 2")
elif False:
    print("Se ejecuta ésta condición 3")
else:
    print("Se ejecuta ésta condición 4")

print("\n Ejemplo 3")
if False:
    print("Se ejecuta ésta condición 1")
elif False:
    print("Se ejecuta ésta condición 2")
elif True:
    print("Se ejecuta ésta condición 3")
else:
    print("Se ejecuta ésta condición 4")

print("\n Ejemplo 4")
if False:
    print("Se ejecuta ésta condición 1")
elif False:
    print("Se ejecuta ésta condición 2")
elif False:
    print("Se ejecuta ésta condición 3")
else:
    print("Se ejecuta ésta condición 4")