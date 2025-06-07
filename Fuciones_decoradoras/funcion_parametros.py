def a(b):
    def c(num1, num2):
        print("El resultado de la operacion es: ")
        b(num1,num2)
        print("Operacion realizada con exito")
    return c

@a
def sumar(num1, num2):
    print(num1 + num2)
    
sumar(40,67)
sumar(100,45)