"""Una panadería vende barras de pan a 3.49€ cada una.
 El pan que no es el día tiene un descuento del 60%. 
 Escribir un programa que comience leyendo el número 
 de barras vendidas que no son del día. Después el 
 programa debe mostrar el precio habitual de una barra 
 de pan, el descuento que se le hace por no ser fresca y 
 el coste final total.
"""
 
pan = float(input("Ingrese el numero de pan vendidas:  ")) 
valorPan = 3.49
descuento = 0.6
panConDescuento = (pan * valorPan) * (1 - descuento)

print("Precio del pan por unidad: ", pan ,'\n' "El descuento del pan: "
, descuento, "%", '\n' "El precio total del pan es: ", panConDescuento)


