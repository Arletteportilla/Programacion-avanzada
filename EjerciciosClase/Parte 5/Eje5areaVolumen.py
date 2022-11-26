"""Escribir una función que calcule el área de un círculo y otra 
que calcule el volumen de un cilindro usando la primera función.
"""
def areaCirculo(radio):
    pi = 3.1415
    return pi*radio**2

def volumenCilindro(radio, altura):
    return areaCirculo(radio)*altura

print(volumenCilindro(3,5))