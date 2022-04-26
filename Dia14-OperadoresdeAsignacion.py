#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 14 - Operadores de Asignación y bucles
#Los operadores de asignación son usados para asignar valores.
#Por ejemplo tengamos en cuanto que en Python el símbolo = se usa para
#almacenar un valor en una variable y a éste proceso se le llama
#asignación o asignar un valor a una variable. En python existen 
#otros modos con los cuales se puede asignar un valor a una variable. 
#Éstos son llamados operadores de asignación y son:

print("Operador \t Ejemplo \t Igual a")
print("  += \t\t x += 3 \t x = x + 3")
print("  -= \t\t x -= 3 \t x = x - 3")
print("  *= \t\t x *= 3 \t x = x * 3")
print("  /= \t\t x /= 3 \t x = x / 3")
print("  %= \t\t x %= 3 \t x = x % 3")
print("  //= \t\t x //= 3 \t x = x // 3")
print("  **= \t\t x **= 3 \t x = x ** 3")

print("\n Ejemplo1")
#El modo más utilizado de éstos operadores es para que una variable aumente
#con base en una acción
print("\n Modo tradicional")
contador = 0
for numeros in [1,2,3,4,5]:
    contador = contador + 5
    print(contador)

print("\n Usando operador de asignación")
contador = 0
for numeros in [1,2,3,4,5]:
    contador += 5 #contador = contador + 5 se reemplaza por contador +=5 
    print(contador)
#el operador de asignación me suma 5 a la variable cada iteración. El bucle
#Itera 5 veces porque le estoy diciendo que lo haga por cada item en la lista


print("\n Ejemplo2")

print("\n Modo tradicional")
contadorInverso = 20
while contadorInverso > 0:
    contadorInverso = contadorInverso - 2
    print(contadorInverso)

print("\n Usando operador de asignación")
contadorInverso = 20
while contadorInverso > 0:
    contadorInverso -= 2
    print(contadorInverso)
#el operador de asignación resta 2 a la variable cada iteración. El bucle
#Itera las veces que sea necesaria hasta que la variable deje de ser mayor a 0