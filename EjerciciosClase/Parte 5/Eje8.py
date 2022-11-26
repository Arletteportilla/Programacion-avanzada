"""Escribir una función que reciba una muestra de números en una lista 
y devuelva un diccionario con su media, varianza y desviación típica.
"""
def cuadrado(*sample):
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(*sample):
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(cuadrado(*sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics(0, 6, 8, 5, 7))
print(statistics(2.5, 6.2, 7.5, 1.3, 5.6, 10.5))
