"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
"""
def cuentaPalabras(texto):

    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def most_repeated(palabras):
    maxPalabra = ''
    maxFrecuencia = 0
    for plabra, frecuencia in palabras.items():
        if frecuencia > maxFrecuencia:
            maxPalabra = plabra
            maxFrecuencia = frecuencia
    return maxPalabra, maxFrecuencia

text = "La gallina turuleca a puesto un huevo, a puesto dos, a puesto tres"
print(cuentaPalabras(text))
print(most_repeated(cuentaPalabras(text)))