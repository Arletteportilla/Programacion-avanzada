"""Escribir un programa que pregunte al usuario 
una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el 
capital obtenido en la inversión.
"""


cantidad = float(input("Cantidad a invertir: "))
interesAnual = 12
numeroAnios = float(input("Numero de Años: "))

totalInversion = (cantidad * 12/100* numeroAnios)
print(totalInversion)
