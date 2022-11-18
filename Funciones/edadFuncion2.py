"""
Crear una funcion que permita conocer el rango de edad
"""

nombre = input("Ingrese su nombre: ")

edad = int(input("Por favor ingrese su edad: "))

def edadCalcular(edad,nombre):
    if edad >= 18 and edad<= 65:
        print("Es mayor de edad")
    elif edad >= 65:
        print("Usted es parte de la 3ra Edad")    
    else:
        print("Es menor de edad")    

edadCalcular(edad)   