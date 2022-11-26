"""Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
nombre = int(input("Ingrese un numero: "))

for nombre in range(nombre, -1, -1):
    print(nombre, end =",")
