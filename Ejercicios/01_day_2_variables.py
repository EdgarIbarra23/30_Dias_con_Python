print("<------------ NIVEL 1 ------------>")

# Día 2: 30 días de programación en Python
first_name = "Edgar"
last_name = "Ibarra"
full_name = "Edgar Fernando Ibarra Cabanzo"
country  = "Colombia"
city = "Barranquilla"
age = 18
year = 2023
is_married = False
is_true = True
is_light_on = ["Car", "TV", "Computer", "Cell Phone"]

print("Mi Nombre es", full_name,"tengo", age ,"años de edad, Actualmente me encuentro Practicando el Lenguaje de Python en el año", year,"Mi Pais de Origen es", country+", Actualmente Vivo en", city+", si actualmente estoy Casado o tengo Novia es", is_married)

print("")
print("<------------ NIVEL 2 ------------>")
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))



print("")
print("----------------------------------------------------------------")
print(len(first_name))
print("La longitud de mi Nombre es:", len(first_name), "y la Longitud de mi Apellido es:", len(last_name))




print("")
print("----------------------------------------------------------------")
num_one = 5
num_two = 4

total = num_one + num_two
print("Suma:",total)

diff = num_two - num_one
print("Resta:",diff)

product = num_two * num_one
print("Multiplicación:",product)

division = num_one / num_two
print("División:",division)

remainder = num_two % num_one
print("Resto:",remainder)

exp = num_one ** num_two
print("Elevación:",exp)

floor_division = num_one // num_two
print("Division de Piso:",floor_division)




print("")
print("----------------------------------------------------------------")
radio_circulo = 30

area_of_circle = 3.1416 * (radio_circulo ** 2)
print("El area del Circulo es de:",area_of_circle)

circum_of_circle = (2 * 3.1416) * radio_circulo
print("La Circunferecnia del Circulo es de:",circum_of_circle)

radio = float(input("Ingrese el Radio del Circulo: "))
area_of_circle_users = 3.1416 * (radio ** 2)
print("Acorde al radio que no dio que",radio,"el Area del Circulo es de:", area_of_circle_users)



print("")
print("----------------------------------------------------------------")
nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese su Apellido: ")
edad = int(input("Ingrese su Edad: "))
ciudad = input("Ingrese su Ciudad: ")

print("")
print("Nombre:", nombre)
print("Apellido:",apellido)
print("Edad:",edad)
print("Ciudad:",ciudad)

print("")
print(f"Señor@ {nombre} {apellido}, con {edad} años de edad y actualmente vive en {ciudad}")
