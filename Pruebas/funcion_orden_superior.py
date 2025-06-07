"""Modulo de funciones superiores"""

def cuadrado(x):
    """Funcion que retorna el cuadrado de un numero"""
    return x * x


def cubo(x):
    """Funcion que retorna el cubo de un numero"""
    return x ** 3


def aplicar_funcion_a_lista(funct, lista):
    """Funcion que retorna una lista con la funcion que pasamos"""
    resultado = []
    for elemento in lista:
        resultado.append(funct(elemento))
    return resultado


lista_numeros = [1, 2, 3, 4, 5]

print(aplicar_funcion_a_lista(cubo,lista_numeros))
print(aplicar_funcion_a_lista(cuadrado,lista_numeros))

### RETORNO DE FUNCIONES ###

def multiplicador(factor):
    """Funcion que retorna la funcion interna"""
    def funcion_interna(numero):
        return numero * factor
    return funcion_interna

multiplicar_por_2 = multiplicador(2)
multiplicar_por_5 = multiplicador(5)

print(multiplicar_por_2(3))
print(multiplicar_por_5(6))
