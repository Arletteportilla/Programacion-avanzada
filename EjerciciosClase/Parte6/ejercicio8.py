"""Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y 
devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes 
a las notas aprobadas."""
def grade(valor0a10):

    if valor0a10 < 5:
        return 'SS'
    elif valor0a10 < 7:
        return 'AP'
    elif valor0a10 < 9:
        return 'NT'
    elif valor0a10 < 10:
        return 'SB'
    else:
        return 'MH'

def aplicarNota(valor0a10):

    sujetos = map(str.upper, valor0a10.keys())
    notas = map(grade, valor0a10.values())
    return dict(zip(sujetos, notas))

print(aplicarNota({'Algebra Lineal':6.5, 'Analisis Matematico':5, 'Sistemas Operativos':3.4, 'Base de datos':8.2, 'Introduccion a redes':9.7, 'Programación':10}))
