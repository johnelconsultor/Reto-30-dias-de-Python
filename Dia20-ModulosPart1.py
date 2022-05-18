#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 20 Modulos Part 1 
#Un modulo es un archivo que contiene un conjunto de códigos o un grupo de funciones
#qué pueden ser incluidas en la aplicación. Un modulo puede ser un archivo que contenga
#Una sóla variable, una función o una base grande de código

print("Creando un modulo")
#Para crear un modulo escribimos nuestro código en un script de python y lo grabamos como
#un archivo .py (que es la extensión de python)

print("Importando un modulo")
#Para importar un modulo usamos la.
#palabra import. ES CLAVE EN PYDROID (El app que estamos usando que TODO ESTE EN LA MISMA CARPETA)
import suma
print(suma.sumaDos(10,20))

print("Importando funciones especifícas")
#Si no queremos importar el modulo completo podemos importar funciones especificas
from suma import restaDos
print(restaDos(10,5))


print("Importar el modulo cambiando su nombre")
#Para facilitar la escritura de codigo podemos cambiar el nombre de un modulo al importarlo
import suma as s
print(s.sumaDos(40,50))

print("Importar una funcion cambiando su nombre")
#Para facilitar la escritura de codigo podemos cambiar el nombre de la funcion al importarla
from suma import restaDos as re
print(re(100,90))

#Mis datadict@s aun nos falta por aprender sobre los modulos




