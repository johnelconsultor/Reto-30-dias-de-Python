#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 15 RETO BÁSICO VIDA EN SEMANAS
#Generaremos una calculadora que le diga al usuario cuánta
#vida le queda en años, meses y semanas
#Elementos
# Expectativa de vida: 75 años
# Año: 365 dias, 12 meses y 52 semanas

#Reto
#Generar una calculadora del BMI que nos solicite los datos

#Tareas
#1 Generar el letrero de bienvenida
print("¿Cuánto te falta para morir?")

#2 Generar las variables que utilizaremos y respecitvos inputs
nombre = input("Introducr tu nombre: ")
añosUsuario = int(input("Introduce tu edad en años: "))
expecativaVida = 75

#3 Generar el cálculo del resultado y almacenarlo en una variable
añosRestantes = expecativaVida - añosUsuario
mesRestantes = añosRestantes * 12
semResrantes = añosRestantes * 52

#4 Entregar al usuario el mensaje final con su expectativa de vida
print(f" {nombre} te quedan de vida \n {añosRestantes} años  \n o {mesRestantes} meses \n o {semResrantes} semanas")
