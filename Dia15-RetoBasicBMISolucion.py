#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 15 RETO BÁSICO CALCULADORA IMC
#La calculadora del índice de masa corporal nos permite conocer el 
#estado de nuestro peso con base en nuestra altura crearemos una
#que brinde mensajes personalizados

#Elementos
#Formula IMC: PESO(KG) / ALTURA (M)**2

#Reto
#Generar una calculadora del BMI que nos solicite los datos

#Tareas
#1 Generar el letrero de bienvenida
print("Calcule su IMC GRATIS")

#2 Generar las variables que utilizaremos y respecitvos inputs
nombre = input("Ingrese su Nombre: ")
altura = float(input("Ingrese su ALTURA en Metros: "))
peso = float(input("Ingrese su PESO en Kilos: "))

#3 Generar el cálculo del resultado y almacenarlo en una variable
imc = round(peso / (altura ** 2))

#4 Entregar al usuario el mensaje final con su BMI Calculado
print(f"{nombre} su IMC es: {imc}")