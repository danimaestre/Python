"""
    La funcion predefinida dir() nos devuelve una lista de nombres ordenados alfabeticamente, son todos los nombre que hay en el espacio de nombres donde se ejecuta esta funcion
"""

from math import acos

def prueba():
    variable_prueba = None
    variable_prueba2 = None
    print(dir())


print(dir()) # --> Primero aparecen los elementos integrados por python y luego el elemento del modulo math acos
print("******************************")
prueba()


import math
espacio_nombres = dir()

if 'math' in espacio_nombres:
    print("math esta en el espacio nombres")
else:
    print("math no esta en el espacio nombres")
    
print(dir())