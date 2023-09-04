# 1. Declara tu edad como variable entera
edad = 18

# 2. Declara tu altura como una variable flotante
altura = 1.67

# 3. Declarar una variable que almacene un número complejo
_complex = 2 + 3j

print("4. Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule el área de este triángulo (área = 0,5 xbxh)")
t_base = float(input("Ingrese la Base: "))
t_altura = float(input("Ingrese la Altura: "))
area_triangulo = 0.5 * t_base * t_altura
print("El Area del Triangulo es ", int(area_triangulo))



print("")
print("----------------------------------------------------------------")
print("5. Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c)")
lado_one = float(input("Ingrese el Valor de Lado 1: "))
lado_two = float(input("Ingrese el Valor de Lado 2: "))
lado_three = float(input("Ingrese el Valor de Lado 3: "))
perimetro_triangulo = lado_one + lado_two + lado_three
print("El Perimetro del Triangulo es ", int(perimetro_triangulo))



print("")
print("----------------------------------------------------------------")
print("6. Obtenga el largo y el ancho de un rectángulo usando el mensaje. Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))")
c_altura = float(input("Ingrese la Altura del Cuadrado: "))
c_ancho = float(input("Ingrese el Ancho del Cuadrado: "))
area_cuadrado = c_altura * c_ancho
perimetro_cuadrado = 2 * (c_altura + c_ancho)
print("EL Area del Cuadrado es: ", int(area_cuadrado), "\nEl Perimetro del cuadrado: ", int(perimetro_cuadrado))



print("")
print("----------------------------------------------------------------")
print("7. Obtenga el radio de un círculo usando el mensaje. Calcula el área (área = pi xrxr) y la circunferencia (c = 2 x pi xr) donde pi = 3,1416")
cir_radio = float(input("Ingrese el Radio del Circulo: "))
cir_area = 3.1416 * (cir_radio ** 2)
cir_circuferencia = 2 * (3.1416 * cir_radio)
print("El Area del Circulo es",cir_area,"\nLa Circuferencia del Circulo es",cir_circuferencia)



print("")
print("----------------------------------------------------------------")

txt_1 = "python"
txt_2 = "dragon"
txt_3 = "Espero que este curso no esté lleno de jerga"

print("8. Encuentre la longitud de 'python' y 'dragon' y haga una comparación.")
print(len(txt_1) == len(txt_2))



print("")
print("----------------------------------------------------------------")
print("9. Utilice un operador para comprobar si 'on' se encuentra tanto en 'python' como en 'dragon'")
print("'on' se encuentra el alguna parte de 'python' ---->","on" in txt_1)
print("'on' se encuentra el alguna parte de 'dragon' ---->","on" in txt_2)



print("")
print("----------------------------------------------------------------")
print("10. Espero que este curso no esté lleno de jerga . Úselo en el operador para verificar si hay jerga en la oración.")
print("'jerga' se encuentra en 'Espero que este curso no esté lleno de jerga' ---->","jerga" in txt_3)



print("")
print("----------------------------------------------------------------")
print("11. No hay ningún 'encendido' tanto en Dragon como en Python.")
print("'Encendido' se encuentra en alguna parte de 'python' ---->","encendido" in txt_1)
print("'Encendido' se encuentra en alguna parte de 'dragon' ---->","encendido" in txt_2)



print("")
print("----------------------------------------------------------------")
print("12. Encuentre la longitud del texto Python y convierta el valor a flotante y conviértalo en cadena")
longitud_txt_1 = str(float(len(txt_1)))
print(longitud_txt_1)
print(type(longitud_txt_1))



print("")
print("----------------------------------------------------------------")
print("13. Los números pares son divisibles por 2 y el resto es cero. ¿Cómo se comprueba si un número es par o no, usando Python?")
numero = int(input("Ingrese Número: "))
if numero % 2 == 0:
    print(f"El Número {numero} es Divisible por 2")
else:
    print(f"El Númerono {numero} es Divisible por 2")



print("")
print("----------------------------------------------------------------")
print("14. Compruebe si la división del piso de 7 por 3 es igual al valor int convertido de 2,7.")
print(7 // 3,"<---- División del piso de 7 por 3")
print(int(2.7),"<---- Valor int convertido de 2,7")
print(7 // 3 == int(2.7))



print("")
print("----------------------------------------------------------------")
print("15. Compruebe si el tipo de '10' es igual al tipo de 10")
print(type('10'), "<---- EL Tipo de '10'")
print(type(10), "<---- EL Tipo de 10")
print(type('10') == type(10))



print("")
print("----------------------------------------------------------------")
print("16. Compruebe si int('9.8') es igual a 10")
try:
    numero_convertido = int('9.8')
    if numero_convertido == 10:
        print("int('9.8') es igual a 10.")
    else:
        print("int('9.8') no es igual a 10.")
except ValueError:
    print("No se puede convertir '9.8' a un entero.")



print("")
print("----------------------------------------------------------------")
print("17. Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el salario de la persona?")
horas = input("Ingrese sus Horas Trabajada: ")
tarifa_horas = input("Ingrese la Tarifa de las Horas: ")
salario = int(horas) * int(tarifa_horas)
print(f"El Salario de la Persona es de {salario}")



print("")
print("----------------------------------------------------------------")
print("18. Escriba un script que solicite al usuario que ingrese el número de años. Calcula el número de segundos que puede vivir una persona. Supongamos que una persona puede vivir cien años.")
años = int(input("Ingrese el número de años: "))
segundo_en_un_año = 31536000
segundos_totales = años * segundo_en_un_año
print(f"Usted tiene {segundos_totales} segundos")




