import math

def a(b):
    def c(*args):
        print("El resultado de la operacion es: ")
        b(*args)
        print("Operacion realizada con exito\n")
    return c

@a
def sumar(num1, num2, num3, num4, num5):
    print(num1 + num2 + num3 + num4 + num5)
    
@a
def restar(num1, num2):
    print(num1-num2)
    
sumar(40,67, 34, 56, 78)
restar(50,67)

def g(b):
    def c(*args, **kwars):
        print("Empieza el calculo: ")
        b(*args, **kwars)
        print("Operacion realizada con exito\n")
    return c

@g
def area_rectangulo(base, altura):
    print(f"El area del rectangulo es: {base * altura}")
    
@g
def area_triangulo(base, altura):
    print(f"El area del triangulo es: {base * altura/2}")
    
@g
def area_circulo(radio):
    print(f"El area del circulo es: {round(math.pi * radio ** 2, 3)}")
    

area_rectangulo(45, 3)
area_circulo(3)
area_rectangulo(altura=10, base=10)

#************************************************

def j(b):
    def c(*args, **kwargs):
        print("Empieza el calculo con args: ")
        b(*args, **kwargs)
        print("Operacion realizada con exito\n")
    return c

@j
def sumar_j(*args):
    '''resultado = 0
    for i in args:
        resultado += i'''
    print(f"La suma de {args} es de: {sum(args)}")
    
sumar_j(20,50,56,120,67, -400)