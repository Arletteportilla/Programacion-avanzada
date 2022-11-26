"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
for n in range(1, 11):
    for i in range(1, 11):
        print(n*i, end="\t")
    print("")