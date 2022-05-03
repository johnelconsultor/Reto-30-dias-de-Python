#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 18 RETO Oradenador de Pizza
#Construir un ordenador de pizza que calcule el monto total
#Con base en los elementos dados

#Elementos
#pizzaPersonaL = 10
#pizzaMediana = 20
#pizzaFamiliar = 40

#costo pepperoni para pequeña $1
#costo pepperoni para las otras $3
#Queso adicional $2

#Tareas
#1 Generar el letrero de bienvenida

#2 Generar las variables que utilizaremos y respecitvos inputs

#3 Generar el cálculo del resultado y almacenarlo en una variable

#4 Imprimir un mensaje personalizado al usuario con el monto total

print("Ordenador de pizzas")
seleccionPizza = input("Seleccione el tamaño con la letra: P,M,N ").lower()
seleccionQueso = input("Quiere queso adicional? Y/N ").lower()

totalPizza = 0
#Costo pizza
if seleccionPizza == "p":
    totalPizza += 10 #Costo pizza
    totalPizza += 1 #Costo pepperoni
elif seleccionPizza == "m":
    totalPizza += 20 #Costo pizza
    totalPizza += 1 #Costo pepperoni
elif seleccionPizza == "f":
    totalPizza += 40 #Costo pizza
    totalPizza += 1 #Costo pepperoni

#Costo adicionales
if seleccionQueso == "y":
    totalPizza += 2 #costoQuejo


print(totalPizza)