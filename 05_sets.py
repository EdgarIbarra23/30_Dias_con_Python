one_set = set()
two_set = {'Edgar', "Ibarra", 18, 1.67}

# Longitud 
print(len(two_set))

print("")
print("----------------------------------------------------------------")
# Buscar si el Elemento que quiero esta en el set

print("Edgar" in two_set)
print("Fernando" in two_set)



print("")
print("----------------------------------------------------------------")
# Agregar otro Elemento en una set
two_set.add("Fernando")
print(two_set, "<---- Un set no es una estructura ordenada - add()")

# No Permite elementos Repetidos
two_set.add("Fernando")
print(two_set, "<---- No Permite elementos Repetidos")



print("")
print("----------------------------------------------------------------")
# Copiar por completo el set y colocarlo en una nueva variable la cual si deseas hacer cambios solo afectara a la copia
copia = two_set.copy()
print(two_set, "<---- Set ORIGINAL")
print(copia, "<---- Set COPIA - copy()")



print("")
print("----------------------------------------------------------------")
# Borrar elementos que uno quiere
two_set.remove(1.67)
print(two_set, "<---- Elimina el Elemento que yo quiera de la Variable original - remove()")

print("")

copia.clear()
print(copia, "<---- Elimina por Completo la Variable Copia - clear()")



print("")
print("----------------------------------------------------------------")
# Concatenacion solo sirve con la Propiedad "union()", no funciona ni con el signo mas(+) o la coma(,)
three_sets = {"JavaScript", "Python", "Java"}
concatenacion = two_set.union(three_sets)

print(concatenacion, "<---- Concatenacion otra Variable - union()")
print(concatenacion.union({"HTML", "CSS"}).union(three_sets), "<---- Concatenacion desde el Print")



print("")
print("----------------------------------------------------------------")
# Diferencia entre dos set con algunos elementos repetidos
print(concatenacion.difference(two_set), "<---- Mostrara los Elementos que no se repiten entre las variables 'concatenacion' y 'two_set' - difference()")