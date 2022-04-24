#JOHN EL CONSULTOR PRESENTA
#Aprende PYTHON desde el Telefóno
#En mi perfil de tiktok encuentran:
#1 Link a mi web donde esta python
#2 Lista de reproducción con el curso

#Dia 11 - Sets / Operaciones
#La definción de sets / conjuntons en python es la misma que la de matemáticas. Un conjunto es una colección de elementos únicos sin orden específico
#Y con ellos podemos realizar las mismas operaciones que se realizan con conjuntos


#print("\n Uniendo Conjuntos")
#Existen diferentes modos de unir conjuntos a continuación veremos los más usados
# conjunto1 = {"cosa1","cosa2","cosa3","cosa4"}
# conjunto2 = {"cosa5","cosa6","cosa7","cosa8"}

#print("\n Utilizando el método union")
#Devuelve un set completamente nuevo por eso se aloja en una variable
# set1 = conjunto1.union(conjunto2)
# print(set1)

#print("\n Utilizando el método update")
#Altera el conjunto original el cuál fue unido con un nuevo conjunto
# conjunto1.update(conjunto2)
# print(conjunto1)

#print("\n Hallando intersecciones entre conjuntos")
#Una intersección es hallar los elementos comunes entre diferentes conjuntos
# conjunto1 = {"cosa1","cosa2","cosa3","cosa4"}
# conjunto2 = {"cosa1","cosa2"}
# print(f"Conjunto1: {conjunto1}")
# print(f"Conjunto2: {conjunto2}")
# print(conjunto1.intersection(conjunto2))

#print("\n Revisando si es superset")
#Un superset (Superconjunto) es un conjuntao que contiene a otro
# print(f"Conjunto1: {conjunto1}")
# print(f"Conjunto2: {conjunto2}")
# print(conjunto1.issuperset(conjunto2))

#print("\n Revisando si es subset")
#Un subset (Subconjunto) es un conjunto que es contenido por otro
# print(f"Conjunto1: {conjunto1}")
# print(f"Conjunto2: {conjunto2}")
# print(conjunto2.issubset(conjunto1))

#print("\n Revisando diferencias entre dos conjuntos")
#Las diferentes entre dos conjuntos son los elementos que no tienen en común
# print(f"Conjunto1: {conjunto1}")
# print(f"Conjunto2: {conjunto2}")
# print(conjunto1.difference(conjunto2)) #Hay diferencias respecto del superset contra el subset
# print(conjunto2.difference(conjunto1)) #No hay diferencias respecto del subset contra el superset

#print("\n Revisando diferencias simétrias entre dos conjuntos")
#El resultado de la diferencia simétrica es un subconjujnto que contiene todos los items de ambos ocnjuntos excepto aquellos que están en ambos a la vez
# print(f"Conjunto1: {conjunto1}")
# print(f"Conjunto2: {conjunto2}")
# print(conjunto1.symmetric_difference(conjunto2)) #Hay diferencias respecto del superset contra el subset

#print("\n Revisando si son diferentes")
#Si ambos conjuntos no tienen items en comun son dispares y eso se puede revisar a través de
# print(f"Conjunto1: {conjunto1}")
# print(f"Conjunto2: {conjunto2}")
# print(conjunto1.isdisjoint(conjunto2)) #Da falso porque ambos tienen items en común
# print(conjunto1.intersection(conjunto2))

