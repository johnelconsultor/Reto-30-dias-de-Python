#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 17 RETO BÁSICO CALCULADORA AÑO BISIESTO
#Crearemos una calculadora que nos diga si un año es
#Bisiesto o no. Un año bisiesto  es aquel que tiene
#Un dia adicional en febrero

#Elementos
#El modo más sencillo de saber si un año bisiesto es:
#Si el año es divisible por 4 y no se puede dividir
#por 100 limpiamente es bisiesto. Adicional si 
#Es divisible por 4, 100 y 400 es Bisiesto

#Tareas
#1 Generar el letrero de bienvenida
print("Calculadora de año bisiesto")

#2 Generar las variables que utilizaremos y respecitvos inputs
año = int(input("Inserte el año: "))

#3 Generar el cálculo del resultado y almacenarlo en una variable
#4 Decirle al usuario qué tipo de año es

if año % 4 == 0:
	if año % 100 == 0:
		if año % 400 == 0:
			print("Es Bisiesto")
		else:
			print("No es Bisiesto")
	else:
		print("Es Bisiesto")
else:
	print("No es Bisiesto")

#5 Probar años 2022, 2024, 2026, 2028

