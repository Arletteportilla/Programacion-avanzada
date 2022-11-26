"""Escribir una función que convierta un número decimal en 
binario y otra que convierta un número binario en decimal.
"""

def cambiarDecimal(n):

    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal


def CambiarBinario(n):

    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)


print(cambiarDecimal('10110'))
print(CambiarBinario(26))
print(cambiarDecimal(CambiarBinario(26)))
print(CambiarBinario(cambiarDecimal('10110')))
