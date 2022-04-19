#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#APP Gratuita en mi descripción de TK

#Dia 9 - Sacar items de listas
#Las listas son estructuras de datos mutables cuyo orden puede ser alterado
# animales = ['perro', 'gato', 'gata', 'toro', 'vaca', 'burro', 'pollo', 'loro', 'gallina']
# print(f"lista inicial: {animales}")

# print("\n Remover items")
#Para sacar items específicos de una lista
# animales.remove("pollo")
# animales.remove("loro")
# animales.remove("gallina")
# print(animales)


# print("\n Remover items usando el método pop")
#remueve el último item por default o alguno que específiquemos
# animales.pop()
# print(animales)
# animales.pop(0)
# print(animales)

# print("\n Remover items usando la palabra clave del")
#La palabra clave del remueve items con índice especificado, rangos o toda la lista
# animales1 = animales.copy()
# animales2 = animales.copy()
# animales3 = animales.copy()

# del animales1[-1] #Borra el último item
# del animales2[-3:] #Borra desde el índice -3 al final
# del animales3 #Borra la lista completa y hace que aparezca el error "lista no definida"

# print(animales1)
# print(animales2)
#print(animales3)

# print("\n Remover items usando el método clear")
#Vacía la lista completamente pero no la borra como la palabra clave del
# animales4 = animales.copy()
# animales4.clear()

# print(f"Lista semi-original {animales}")
# print(f"Lista vacia {animales4}")

# #Se preguntarán ustedes qué más se puede hacer, pués con las listas y con todas las estructuras de datos en python en general hay un montón de cosas si bien veremos métodos adicionales les recuerdo que usando la documentación encuenrtran todo más fácil