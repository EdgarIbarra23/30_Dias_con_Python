primera_forma = list()
segunda_forma = []

lista_int = [23, 23, 1, 50, 30, 18]
lista_str = ["Hola", "Mundo", "De", "Python"]
lista_mutante = [18, 1.67, "Edgar", "Ibarra", "Python"]



# len() = Longitud de una lista
print(len(lista_int))
print(len(lista_str))
print(len(lista_mutante))



# Saber un Elemento de la List de acuerdo a su Posicion
print("")
print("----------------------------------------------------------------")
print(lista_int[0])
print(lista_int[1])
print(lista_int[-1])

print("")
print(lista_str[0])
print(lista_str[2])
print(lista_str[-1])

print("")
print(lista_mutante[0])
print(lista_mutante[3])
print(lista_mutante[-1])



# Count() = Saber cuantas veces se esta repitiendo un Elemento en la propia Lista
print("")
print("----------------------------------------------------------------")
print(lista_int.count(23))
print(lista_str.count("Hola"))
print(lista_mutante.count("Python"))



# Colocar los Elementos de una Lista por separado en diferentes Variables
print("")
print("----------------------------------------------------------------")
edad, altura, nombre, apellido, lenguaje_practicante = lista_mutante
print(edad)
print(altura)
print(nombre)
print(apellido)
print(lenguaje_practicante)


# Concatenar Listas
print("")
print("----------------------------------------------------------------")
print(lista_int + lista_str + lista_mutante, "<---- En una Sola Lista TODOS")
print(lista_int, lista_str, lista_mutante, "<---- En Diferentes Listas TODOS pero Juntas")



# Insertar mas elementos en una lista
print("")
print("----------------------------------------------------------------")
print(lista_mutante)

# Insertar mas elementos en una lista y este quede en la ultima posicion
lista_mutante.append(2023)
print(lista_mutante, "<---- Insertar mas elementos en una lista y este quede en la ultima posicion")


# Insertar mas elementos en una lista y este quede en cualquier posicion que deseemos
lista_mutante.insert(3, "Fernando")
print(lista_mutante, "<---- Insertar mas elementos en una lista y este quede en cualquier posicion que deseemos")




print("")
print("----------------------------------------------------------------")
print("Las tuplas son como listas pero constantes, quiere decir que no se pueden agregar, Cambiar, Eliminar elementos, para hacerlo hay que convertirlos en listas y regresarlos a tuplas.")