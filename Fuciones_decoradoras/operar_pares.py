

def operarConPares(operacion):
    def wrapper(*args, **kwargs):
        soloPares= list(filter(lambda num: num % 2 == 0, args))
        resultado = operacion(*soloPares, **kwargs)
        #print(f"El resultado de la operacion es: {resultado}")
        return resultado
    return wrapper

#Llamada con decorador

@operarConPares
def sumar(*args):
    acc = 0
    for num in args:
        acc += num
    return acc

@operarConPares
def multiplicar(*args):
    acc = 1
    for num in args:
        acc *= num
    return acc

#LLamada normal

sumarPares = operarConPares(sumar)(1, 5, 2, 8)
#sumarPares(1, 22, 55, 22)

multiplicarPares = operarConPares(multiplicar)(5, 4, 7, 8, 9)

print(f"El resultado de la operacion es: {sumar(3, 7, 8, 20, 56, 79, 44)}")
print(f"El resultado de la operacion es: {sumarPares}")

print(f"El resultado de la multiplicacion es: {multiplicar(5, 7, 8, 8, 10)}")

print(f"El resultado de la multiplicacion es: {multiplicarPares}")