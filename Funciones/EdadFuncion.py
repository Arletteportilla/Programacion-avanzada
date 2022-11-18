"""
Crear una funcion que permita conocer el rango de edad
"""

nombre = input("Ingrese su nombre: ")

edad = int(input("Por favor ingrese su edad: "))

def edadCalcular(int):
    global edad, nombre  #para utilizar los datos q estan afuera
    if edad >= 18 and edad<= 65:
        print(nombre,"Es mayor de edad")
    elif edad >= 65:
        print(nombre,"Usted es parte de la 3ra Edad")    
    else:
        print(nombre,"Es menor de edad")    

edadCalcular(edad)   
