# Variables

variable_string = "Estoy Creando una Variable String en Python"
variable_int = 3
variable_float = 3.5
variable_bool = True
variable_array = ['HTML', "CSS", 'JS', 'Python', 10, 8, 5, 2]
variable_objeto = {
    'Nombre' : "Edgar",
    'Apellido' : "Ibarra",
    "Edad" : 18,
    "Mes de Nacimiento" : 'Septiembre'
}

variable_suma = variable_int + variable_float

print(variable_string)
print(variable_int)
print(variable_float)
print(variable_bool)
print(variable_suma)
print(variable_array)
print(variable_objeto)
print("----------------------------------------------------------------")

# Variables en una Sola LINEA
nombre, apellido, lenguaje, edad = "Edgar", "Ibarra", "Pyhton", 18

print("Mi nombre es:",nombre,apellido,", mi edad:",edad,".Y estoy Practicando el Lenguaje de Programación:", lenguaje)
print("----------------------------------------------------------------")

# Concatenación: es con la Coma(,)
print(variable_string,":", variable_bool)
print("----------------------------------------------------------------")

# Funciones del Sistema
print(len(variable_string))
print("----------------------------------------------------------------")
