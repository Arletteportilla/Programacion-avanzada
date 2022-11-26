"""Imagina que acabas de abrir una nueva cuenta de ahorros 
que te ofrece el 4% de interés al año. Estos ahorros debido 
a intereses, que no se cobran hasta finales de año, se te 
añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de 
dinero depositada en la cuenta de ahorros, introducida por 
el usuario. Después el programa debe calcular y mostrar por 
pantalla la cantidad de ahorros tras el primer, segundo y
 tercer años. Redondear cada cantidad a dos decimales.
"""

dinero = float(input("Ingrese la cantidad de dinero: "))
interesAnio = 0.04
numeroAnios = dinero * (1 + interesAnio)
print("Balance del primer año:" + str(round(numeroAnios, 2)))
numeroAnios2 = numeroAnios* (1 + interesAnio)
print("Balance del segundo año:" + str(round(numeroAnios2, 2)))
numeroAnios3 =  numeroAnios2 * (1 + interesAnio)
print("Balance tras el tercer año:" + str(round(numeroAnios3, 2)))


