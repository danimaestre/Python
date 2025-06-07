'''
    Los "NAME SPACES" son contenedores o colecciones de idetificadores unicos que permiten organizar el codigo en areas evitando asi conflictos de nombres. Son como separadores como una caja con diferentes compartimientos y ahi podriamos ir organizando diferentes tipos de cosas con el fin de que no se mezcle todo. Son temas importantes de organizacion. En python los espacios de nombres estan almacenados en diccionarios. Cada modulo tiene sus propios diccionarios de espacios de nombres

'''

# Alcance local --> alcance de un elemento dentro de una funcion

nombre = "PCMaster"  # --> variable global

def imprimir_nombre():
    nombre = "Programacion facil"  # --> variable local
    print(nombre)

imprimir_nombre()
print(nombre) # --> da error nombre es alcance local dentro de la funcion

def funcion():
    a = 10
    b = "hola"
    c = 10.56
    # Imprime las variables locales en forma de diccionario
    print(locals( ))
    
funcion()

# Alcance global: --> alcance de un elemento fuera de una funcion, es acesible desde dentro de una funcion

print(globals()) # --> Imprime diccionario global

# diccionario de un modulo
import random
print(random.__dict__)