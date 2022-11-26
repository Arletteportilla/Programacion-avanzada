"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
inversion = int(input("Ingrese la cantidad a invertir: "))
interesAnual= int(input("Ingrese el interes anual: "))
anios = int(input("Ingrese el numero de años: "))

for i in range(anios):
    inversion *= 1 + interesAnual / 100 
    print("Capital tras " + str(i + 1) + " años: " + str(round(inversion, 2)))