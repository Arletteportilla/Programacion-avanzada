"""
pedir una nota al usuario 
si la nota es menor a 10 y mayor o igual a 9, imprimir Excelente.
Si la nota es menor a 9 y mayor o igual a 8 , imprimir Muy bueno,
Si la nota es menor a 8 y mayor o igual a 7, imprimir bueno,
Si la nota es menor a 7 imprimir Reprobado """

nota=float(input("Ingrese su calificacion:"))

if nota>=9 and nota <= 10:
    print(f"{nota:} excelente")
elif nota>=8 and nota<=9:
    print(f"{nota:} Muy bueno")
elif nota>=7 and nota<=8:
    print(f"{nota:} bueno")
elif nota>=6 and nota<=7:
    print(f"{nota:} Reprobado")
else:
    print("Nota desconocida") 