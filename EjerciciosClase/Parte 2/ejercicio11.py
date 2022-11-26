"""Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla
  una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
   el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""
nombre = str(input("Ingrese el nombre del producto: "))
precio = float(input("Ingrese el precio del producto con 6 digitos y 2 decimales : "))
unidades = int(input("Ingrese el numero de unidades con tres digitos:  "))

print("El precio por unidad es: ",nombre, precio, "$")
print("Las unidades de el producto es: ",nombre, unidades)
print("el precio total del producto es: ",nombre, precio * unidades, "$")

