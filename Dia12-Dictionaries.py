#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 12 - Diccionarios / Dictionaries
#Los diccionarios hacen parte de las estructuras de almacenamiento de datos en python y son una colección desordenada, modificable (mutable) de registros en la forma(llave:valor)
#La llave: Hace referencia a una llave única ligada a un valor (SIEMPRE DEBE SER ÚNICA)
#El valor: Hace referencia al valor almacenado que cuenta con una llave única para ser hallado

print("\n Creando diccionarios")
#Para crear diccinarios utilizamos las {} 
print("\n Diccionario vacio")
vacio = {}

print("\n Diccionario lleno")
#Dentro del diccionario cada registro estará almacenado del modo: {llave:valor, llave2:valor2}
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

# print("Midiendo el largo del diccionario")
# print(f"Diccionario 'Persona': {len(persona)}")

# print("\n Accediento a items en el diccionario")
# print("Accediendo a un valor")
#Podemos acceder a valores de un diccionario haciendo referencia a sus llaves
# print(persona['nombre'])
# print(persona['apellido'])
# print(persona['edad'])
# print(persona['habilidades'])

# print("\n Accediento a items en el diccionario con el método .get")
# print(persona.get('nombre'))
# print(persona.get('apellido'))
# print(persona.get('edad'))
# print(persona.get('habilidades'))

# print("\n Añadiendo valores a un diccinario con una nueva llave")
# persona["cargo"] = "Gerente de Consultoria" #Se le asigna una llave única y da el valor
# print(persona)

# print("\n Añadiendo valores a una lista existente")
# persona["habilidades"].append("Tableu")
# print(persona)

# print("\n Modificando valores existentes")
# persona["cargo"] = "Gte Senior Consultoria"
# persona["habilidades"][3] = "Powerpoint" #Modifiqué donde decía "Ppt"
# print(persona)


# print("\n Sacando valores del diccionario")
# print("Sacando valores del diccinario usando .pop('llave')")
#el método .pop("llave") saca el item especificando la llave
# persona.pop("cargo")

# print("\n Sacando valores del diccionario usando .popitem()")
#El método .popitem() saca el último item en el diccionario
# persona.popitem()

# print("\n Sacando valores del diccionario usando la palabra clave del")
#Borra un valor específicado con una llave
# del persona["habilidades"]

# print(persona)

# #Ya aprendimos cómo crear, meter items, modificar items y sacar items, en el siguien tiktok vermeos otros métodos que nos podrían servir con los diccionarios

