#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 12 - Diccionarios / Dictionaries
#Los diccionarios hacen parte de las estructuras de almacenamiento de datos en python y son una colección desordenada, modificable (mutable) de registros en la forma(llave:valor)
#La llave: Hace referencia a una llave única ligada a un valor (SIEMPRE DEBE SER ÚNICA)
#El valor: Hace referencia al valor almacenado que cuenta con una llave única para ser hallado

#Ejemplo de diccionario
persona = {
    'nombre':'John',
    'apellido':'Arias',
    'edad':32,
    'país':'Colombia',
    'casado':True,
    'habilidades':['Excel', 'BI', 'PP', 'PPt', 'Python'],
    'dirección':{
        'calle':'Siempre viva 123',
        'codigozip':'1111111'
    }
    }
#Ejemplo de que el diccionario puede guardar diferentes tipos de datos y estructuras de datos también


# print("\n Viendo si una llave específica existe en el diccionario")
#Para revisar si hay una llave en el diccionario usamos la palabra clave in
# print("nombre" in persona)
# print("segundoApellido" in persona)
# print("Excel" in persona["habilidades"]) #Revisar si dentro de la lista que esta en el diccionario


# print("\n Generando copias de un diccionario")
#Para geberar ciouas dek diccionario utilizamos el método .copy
# persona2 = persona.copy()
# persona3 = persona.copy()

# print("\n Limpiando el diccionario")
#Si quiero dejar el diccionario sin nada por dentro usamos el método .clear()
# print(persona2.clear())

# print("\n Borrando el diccionario")
#Para borrar un dicionario usamos la palabra clave del
# del persona3
#print(persona3) #Lanza error porque el diccionario ya no existe al momento de imprimir

# print("\n Cambiando el diccionario a una lista de valores")
# print(persona.items())

# print("\n Obtener todas las llaves en el diccionario")
#Podemos sacar todas las llaves nada más con el método .keys()
# print(persona.keys())

# print("\n Obtener todas los valores en el diccionario")
#Podemos sacar todas las llaves nada más con el método .keys()
# print(persona.values())

# #Ya son unos expertos en diccionarios