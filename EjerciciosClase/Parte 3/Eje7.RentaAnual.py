"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
rentaAnual = float(input("Ingrese su renta anual: "))
if rentaAnual < 10000:
    print("El tipo impositivo es 5%")
elif rentaAnual  < 20000:
    print("El tipo impositivos es 15%")
elif rentaAnual < 35000:
    print("El tipo impositivo es 20%")
elif rentaAnual < 60000:
    print("El tipo impositivo es 30%")
else: 
    print("El tipo impositivo es 45%") 

