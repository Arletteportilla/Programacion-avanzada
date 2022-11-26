"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales 
o superiores a $1000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos 
mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

edad = int(input("ingrese su edad: "))
InMen = float(input(" Ingrese los ingresos mensuales: "))

if edad > 16  and InMen >= 1000:
    print("Si tiene que atribuir al impuesto")
else:
    print("No tiene que atribuir al impuesto")