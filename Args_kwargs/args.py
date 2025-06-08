
def crear_lista(*args):
    # Creamos una lista vacia
    lista = []
    # Añadimos los datos a la lista
    for i in args:
        lista.append(i)
        
    return lista

# Llamamos a la funcion
llamada = crear_lista(3,67,89,78,45,34,67)

# Imprimimos la lista
print(f"Los valores de la lista son: {llamada}")

def funcion(*args):
    
    # Imprimimos la tupla generada
    print(args)
    # Comprobamos el tipo de dato que es
    print(type(args))
    
funcion(10, 20)

def f_objetos(*objetos):
    print(objetos)
    
f_objetos("hola", 4, 7.9, True)

def funcion2(a, b, *args, c= 56):
    print(a, b, args, c)
    
funcion2(2,4, 6,7,98)