def funcion():
    pass
# Las funciones son objetos
print(type(funcion))

def a():
    print("Funcion A ejecutada")
    
def b(funcion):
    print("Se ha inciado la funcion")
    funcion() # LLama a la funcion que se pasa como argumento (objeto invocable)
    print("Funcion B ejecutada")
    
# Llamada a la funcion 'b' pasando como argumento la funcion 'a'

b(a) #--> a es una funcion: (objeto invocable, callable)
# b(10) # TypeError: 'int' object is not callable

# **************************************************************

# Se esta repitiendo mucho codigo innecesario. Aqui entran en juego las funciones decoradoras

def sumar():
    print("El resultado de la operacion es:")
    print(10 + 10)
    print("Operacion realizada con exito")
    
def restar():
    print("El resultado de la operacion es:")
    print(20 + 10)
    print("Operacion realizada con exito")


def multiplicar():
    print("El resultado de la operacion es:")
    print(45 * 10)
    print("Operacion realizada con exito")


def dividir():
    print("El resultado de la operacion es:")
    print(10 / 10)
    print("Operacion realizada con exito")
    
# **************** USO DE FUNCION DECORADORA *****************

def decoradora(funcion_parametro):
    print("El resultado de la operacion es:")
    funcion_parametro()
    print("Operacion realizada con exito")

# Llamada a funcion decoradora: Hay un problema que las funciones se ejecutan automaticamente sin llamarlas en el codigo

@decoradora   
def sumar2():
    print(10 + 10)
   
@decoradora    
def restar2():
    print(20 + 10)

@decoradora
def multiplicar2():
    print(45 * 10)

@decoradora
def dividir2():
    print(10 / 10)
    
'''
    Para solucionar el problema Estructura funcion decoradora:
        def decoradora(funcion_parametro):
            def interna():
                #codigo de la funcion interna
            return interna

'''

def decoradora_muestra(funcion_parametro):
    def interna():
        # codigo
        pass
    return interna

# Forma simplificada de expresarla

def a(b):
    def c():
        # codigo
        pass
    return c

def decoradora(funcion_parametro):
    def interna():
        print("El resultado de la operacion es:")
        funcion_parametro()
        print("Operacion realizada con exito")
    return interna

@decoradora
def sumar():
    print(23 + 56)
    
sumar()




   



