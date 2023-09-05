
print("1. Concatene la cadena 'Treinta', 'Días', 'De', 'Python' en una sola cadena, 'Treinta días de Python'")
Con_1_1 = "Treinta"
Con_1_2 = "Dias"
Con_1_3 = "De"
Con_1_4 = "Python"
print(Con_1_1, Con_1_2.lower(), Con_1_3.lower(), Con_1_4, "<---- Result")



print("")
print("----------------------------------------------------------------")
print("2. Concatene la cadena 'Codificación', 'Para', 'Todos' en una sola cadena, 'Codificación para todos'")
Con_2_1 = "Codificación"
Con_2_2 = "Para"
Con_2_3 = "Todos"
print(Con_2_1, Con_2_2.lower(), Con_2_3.lower(), "<---- Result")



print("")
print("----------------------------------------------------------------")
print('3. Declare una variable denominada empresa y asígnele un valor inicial "Codificación para todos"')
empresa = "Codificación para todos"



print("")
print("----------------------------------------------------------------")
print("4. Imprima la variable empresa usando print()")
print(empresa, "<---- Result")



print("")
print("----------------------------------------------------------------")
print("5. Imprima la longitud de la cadena de la empresa utilizando el método len() e print() .")
print(len(empresa), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("6. Cambie todos los caracteres a letras mayúsculas usando el método Upper()")
print(empresa.upper(), "<---- Result with upper()")



print("")
print("----------------------------------------------------------------")
print("7. Cambie todos los caracteres a letras minúsculas usando el método lower()")
print(empresa.lower(), "<---- Result wiht lower()")



print("")
print("----------------------------------------------------------------")
print("8. Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All")

txt_1 = "coding for all"

print(txt_1, "<---- Original")
print(txt_1.capitalize(), "<---- capitalize()")
print(txt_1.title(), "<---- title()")
print(txt_1.swapcase(), "<---- swapcase()")



print("")
print("----------------------------------------------------------------")
print("9. Corte (corte) la primera palabra de la cadena Coding For All")
print(txt_1[1:], "<---- Result")



print("")
print("----------------------------------------------------------------")
print("10. Compruebe si la cadena Coding For All contiene una palabra Codificación utilizando el método index, find u otros métodos.")
print("Codificacion" in txt_1, "<---- Result")



print("")
print("----------------------------------------------------------------")
print("11. Reemplace la palabra coding en la cadena 'coding for all' por Python")
print(txt_1.replace("coding", "Python"), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("12. Cambie 'Python for Everyone' a 'Python for All' usando el método de reemplazo u otros métodos")
txt_2 = "Python for Everyone"
print(txt_2)
print(txt_2.replace("Python for Everyone",'Python for All'), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("13. Divida la cadena 'Python for All' usando el espacio como separador split()")
print(txt_1.split(' '), "<---- Result with split()")



print("")
print("----------------------------------------------------------------")
print('14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena por coma.')
txt_3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(txt_3.split(', '), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("15. ¿Cuál es el carácter en el índice 0 en la cadena 'Coding For All'?")
print(txt_1.title()[0], "<---- Result")



print("")
print("----------------------------------------------------------------")
print("16. ¿Cuál es el último índice de la cadena 'Coding For All'?")
print(txt_1.title()[-1], "<---- Result")



print("")
print("----------------------------------------------------------------")
print('17. Qué carácter está en el índice 10 en la cadena "Coding For All"')
print(txt_1.title()[10], "<---- Result")



print("")
print("----------------------------------------------------------------")
print('18. Cree un acrónimo o una abreviatura para el nombre "Python For All"')
txt_4 = "Python For All"
print("".join(iniciales[0].upper() for iniciales in txt_4.split()), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("19. Cree un acrónimo o una abreviatura para el nombre 'Coding For All'")
txt_1_1 = txt_1.title()
print("".join(abreviatura[0].upper() for abreviatura in txt_1_1.split()), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("20. Utilice el índice para determinar la posición de la primera aparición de C en 'Coding For All'")
print(txt_1_1.rindex("C"), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("21. Utilice el índice para determinar la posición de la primera aparición de F en Coding For All'")
print(txt_1_1.rindex("F"), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("22. Utilice rfind() para determinar la posición de la última aparición de l en Coding For All People")
txt_5 = "Coding For All People"
print(txt_5.rfind("l"), "<---- Result")




print("")
print("----------------------------------------------------------------")
print("23. Utilice index o find para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No se puede terminar una oración con porque porque porque es una conjunción'")

oracion = "No se puede terminar una oración con porque porque porque es una conjunción"
print(oracion.find("porque"), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("24. Utilice rindex para encontrar la posición de la última aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'")
print(oracion.rindex('porque'), "<---- Result")



print("")
print("----------------------------------------------------------------")
print('25. Elimina la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque es una conjunción".')
oracion_parte_1 = oracion[0:36]
oracion_parte_2 = oracion[58:]

print(oracion_parte_1, oracion_parte_2, "<---- Result, First Form")
print(oracion.replace("porque porque porque ", ''),"<---- Result, Second Form")



print("")
print("----------------------------------------------------------------")
print("26. ¿''Coding For All' comienza con una subcadena 'Coding' ?'")
print(txt_1_1.startswith("Coding"), "<---- Result with startswith()")



print("")
print("----------------------------------------------------------------")
print("27. ¿'Coding For All' termina con una 'Coding' de subcadena ?")
print(txt_1_1.endswith('Coding'), "<---- Result with endswith()")



print("")
print("----------------------------------------------------------------")
print("28. 'Coding For All', elimina los espacios finales izquierdo y derecho en la cadena dada.")
print(txt_1_1.replace(' ', ''), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("29. ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier(), 30DíasDePython o treinta_días_de_python?")

print("30DiasDePython".isidentifier(), "<---- Result for 30DiasDePython")
print("treinta_días_de_python".isidentifier(), "<---- Result for treinta_días_de_python")



print("")
print("----------------------------------------------------------------")
print("30. La siguiente lista contiene los nombres de algunas de las bibliotecas de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con una cadena de espacio.")
bibliotecas_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(', '.join(bibliotecas_python), "<---- Result")



print("")
print("----------------------------------------------------------------")
print("31. Utilice la secuencia de escape de nueva línea para separar las siguientes oraciones" '''
I am enjoying this challenge.
I just wonder what is next.
''')
print("I am enjoying this challenge. <---- Result\nI just wonder what is next.", "<---- Result")



print("")
print("----------------------------------------------------------------")
print("32. Utilice una secuencia de escape de tabulación para escribir las siguientes líneas" '''
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
''')

print("Name\tAge\tCountry\t        City", "<---- Result")
print("Edgar\t18\tColombia\tBarranquilla", "<---- Result")



print("")
print("----------------------------------------------------------------")
print("33. Utilice el método de formato de cadena para mostrar lo siguiente: The area of a circle with radius 10 is 314 meters square.")
radius = 10
area = 3.14 * radius ** 2
print(f"El Area de un Circulo con Radio {radius} es {int(area)} metros Cuadrados", "<---- Result")



print("")
print("----------------------------------------------------------------")
print("34. Haga lo siguiente utilizando métodos de formato de cadena:"'''
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144''')

num1 = 8
num2 = 6
print("")
print("------ Result ------")
print(f"{num1} + {num2} =", num1+num2, f"\n{num1} - {num2} =", num1-num2, f"\n{num1} * {num2} =", num1*num2, f"\n{num1} / {num2} =", num1/num2, f"\n{num1} % {num2} =", num1%num2, f"\n{num1} // {num2} =", num1//num2,f"\n{num1} ** {num2} =", num1 ** num2)