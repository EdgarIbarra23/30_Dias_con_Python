one_string = "Mi String"
two_string = "Mi otro String"

# La Longitud de el String
print("----------------------------------------------------------------")
print(len(one_string))
print(len(two_string))

# Concatenacion
print("----------------------------------------------------------------")
print(one_string, two_string)

# Otras Dos formas de Concatenar llamada "Formateo" y ayuda a la practica
print("----------------------------------------------------------------")
nombre, apellido, edad = "Edgar", "Ibarra", 18
print("Mi nombre Completo es {} {} y tengo {} años - con .format".format(nombre, apellido, edad))
print(f"Mi nombre Completo es {nombre} {apellido} y tengo {edad} años - con .format pero mas FACIL")

# colocamos pocentaje y al lado la letra que haga referencia al tipo de Dato
"""
%s - String
%d - Integers
%f - Floating
"""
print("Mi nombre Completo es %s %s y tengo %d años - con Porcentaje" %(nombre, apellido, edad))

# String con Salto de Linea
print("----------------------------------------------------------------")
string_salto_linea = "Este es un String\ncon Salto de linea"
print(string_salto_linea)

# String con Tabulacion
print("----------------------------------------------------------------")
string_tab = "\t Este es un String con Tabulacion"
print(string_tab)

# Cortar String
print("----------------------------------------------------------------")
lenguage = "Python"

one_slice = lenguage[1:3]
print(one_slice)

two_slice = lenguage[1:]
print(two_slice)

three_slice = lenguage[-2]
print(three_slice)

four_slice = "JavaScript"[-1]
print(four_slice)

# Revertir el String
print("----------------------------------------------------------------")
one_reversed_string = lenguage[::-1]
print(one_reversed_string)

two_reversed_string = "JavaScript"[::-1]
print(two_reversed_string)

# Funciones del Sistema
print("----------------------------------------------------------------")
lenguage_funciones = "python"
lenguage_funciones_Mayusculas = "PYTHON"

# capitalize() = sirve para colcar la PRIMERA letra del String en Mayuscula
print(lenguage_funciones.capitalize(), "<----- coloca la PRIMERA letra del String en Mayuscula - capitalize()")



# upper() = sirve para colocar TODAS las letras del String en Mayusculas
print("")
print(lenguage_funciones.upper(), "<----- Coloca TODAS las letras del String en Mayusculas - upper()")



# isupper() = sirve para comprobar si el TODO el String esta en Mayusculas
print("")
print(lenguage_funciones.isupper(), "<----- Comprobar si el TODO el String esta en Mayusculas - isupper()")
print(lenguage_funciones_Mayusculas.isupper())
# En este caso estoy conviertiendo el "python" en Mayusculas y enseguida comprobando si esta en Mayusculas
print(lenguage_funciones.upper().isupper()) 



# casefold() = sirve para colcar TODAS las letras del String en Minusculas
# lower() = sirve para colcar TODAS las letras del String en Minusculas
print("")
print(lenguage_funciones_Mayusculas.casefold(), "<----- Colca TODAS las letras del String en Minusculas - casefold()")
print(lenguage_funciones_Mayusculas.lower(), "<----- Colca TODAS las letras del String en Minusculas - lower()")



# islower() = sirve para comprobar si el TODO el String esta en Minusculas
print("")
print(lenguage_funciones.islower(), "<----- Comprobar si el TODO el String esta en Minusculas - islower()")
print(lenguage_funciones_Mayusculas.islower())
# En este caso estoy conviertiendo el "PYTHON" en Minusculas y enseguida comprobando si esta en Minusculas
print(lenguage_funciones_Mayusculas.lower().isupper())



# count() = sirve para contar cuantas cantidades hay en el String dependiente del valor que busque.
# En este caso estoy buscando cuantas "t" hay en el variable con valor "python"
print("")
print(lenguage_funciones.count("t"), "<----- Buscando cuantas 't' hay en el variable con valor 'python' - count()")



# isnumeric() = sirve para Saber si el String es un Integer o int
print("")
print(lenguage_funciones.isnumeric(), "<----- Saber si el String es un Integer o int - isnumeric()")
print("Número 1".isnumeric())
print("1 dulce".isnumeric())
print("1".isnumeric())
print("1.2".isnumeric())



# startswith() = sirve para preguntar si el String COMIENZA con cierta letra o palabra
print("")
# En este caso estoy Preguntando si "python" comienza con "py"
print(lenguage_funciones.startswith("py"), "<----- Estoy Preguntando si 'python' comienza con 'py' - startswith()")

# y en este otro estoy Preguntando si "PYTHON" comienza con "py"
print(lenguage_funciones_Mayusculas.startswith("py"), "<----- Estoy Preguntando si 'PYTHON' comienza con 'py'")



# endswith() = sirve para preguntar si el String TERMINA con cierta letra o palabra
print("")
# En este caso estoy Preguntando si "python" Termina con "on"
print(lenguage_funciones.endswith("on"), '<----- Estoy Preguntando si "python" Termina con "on" - endswith() ')
# y en este otro estoy Preguntando si "PYTHON" Termina con "on"
print(lenguage_funciones_Mayusculas.endswith("on"), '<----- Estoy Preguntando si "PYTHON" Termina con "on"')



# join() = convierte toda una list a una linea de String concatenada
print("")
list_string = ["HTML", "CSS", "JavaScript", "Python"]
print(' '.join(list_string), "<----- Convierte toda una list a una linea de String concatenada - join()")



# replace() = renombra toda o una Parte del String
print("")
# En este caso estoy cambiando todo el String que tiene valor "python" a "JavaScript"
print(lenguage_funciones.replace("python","JavaScript"), "<----- Renombra todo el String - replace()")
# y en este otro estoy cambiando solo donde se escuentre "py" dentro del String "python" a "dos" 
print(lenguage_funciones.replace("py", "dos"), "<----- Renombra una Parte del String - replace()")



# split() = sirve para convertir todo el String en una List
print("")
print(lenguage_funciones.split(), "<----- Convertir todo el String en una List - split()")
