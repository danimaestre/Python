'''
    Gracias a la palabra "global" podemos hacer que una variable global sea utilizable dentro de un ambito local.
    
    Podemos usar "global" para que una variable local se convierta en global con el fin de poder acceder a ella desde fuera

'''

nombre = "PCMaster"  # --> variable global

def imprimir_nombre():
    global nombre
    nombre = "Programacion facil"  # --> variable local
    print(nombre)

imprimir_nombre()  # Programacion Facil
print(nombre)       # PCMaste, con global --> Programacion facil se reasigna la variable despues de la funcion

def funcion():
    global a 
    a = 10
    
funcion()
print(a) # --> Se puede acceder a a porque la declaramos como global dentro de un ambito local(funcion)

''' Cuidado con el uso de "global" 
    El siguiente ejemplo es un ejemplo incorrecto es un codigo propenso a errores. Si no llamamos a la funcion nos imprime 1 y nos daria varios resultados:
'''
var = 1

def foo():
    global var
    var = 12
    print(var)
    
foo()
print(var)

''' Ejemplo correcto de uso global:  '''

var = 1

def foo():
    print(var)
    return 23
    
var = foo()
print(var)