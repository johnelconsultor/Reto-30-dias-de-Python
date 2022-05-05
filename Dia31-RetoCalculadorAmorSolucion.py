#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 19 RETO Calculadora del amor
#Vamos a crear un programa que calcula la compatibilidad
#De dos personas utilizando un método de revista de compras
#Por Catálogo

#Elementos
#Vamos a agarrar dos nombres de personas, chequear el número de las letras
#Que se repiten en la palabra VERDADERO, después se hace lo mismo con la
#Letra amor y al final las cantidades se combinan para hacer un número final
#que llamaremos numeroDelAmor

#Si el númeDelAmor es menor a 10 o mayor que 90 la pareja es perfecta
#Si el númeDelAmor está entre 40 y 50 el amor es normal
#Si es cualquier otro no son compatibles

#Tareas
#1 Generar el letrero de bienvenida

#2 Generar las variables que utilizaremos y respecitvos inputs

#3 Generar el cálculo del resultado y almacenarlo en una variable

#4 Imprimir un mensaje personalizado al usuario


from itertools import count


nombre = "john"
nombre2 = "daniela"
lista = ["amor", "verdadero"]

contador = 0
contador2 = 0

for items in lista:
    for palabras in items:
        contador += nombre.count(palabras)
        contador2 += nombre2.count(palabras)
        print(palabras, nombre2)
        print(nombre2.count(palabras))

