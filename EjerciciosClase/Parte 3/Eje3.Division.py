"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error."""

dividendo = float(input("Ingrese un numero dividiendo: "))
divisor = float(input("Ingrese un numero divisor: "))
div = int(dividendo/divisor)
if div == 0:
    print ("ERROR")
else:
    print(dividendo/divisor)
