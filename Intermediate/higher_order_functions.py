### Funciones de orden superior (Higher Order Functions) ###

# Son funciones que hacen cosas con funciones dentro. Funciones que son capaces de ejecutar funciones. Son ciudadanos de 1ª clase, estan en lo mas alto de la jerarquia a la hora de tratar con propiedad este tipo de dato dentro del lenguaje de programacion.


def sum_one(value):
    return value + 1

def sum_five(value):
    return value * 5

def sum_two_values_and_one(first_value, second_value, f_sum_one):
    return f_sum_one(first_value + second_value)

print(sum_two_values_and_one(30, 40, sum_one))
print(sum_two_values_and_one(30, 40, sum_five))

### CLOSURES ###

## Funciones de orden superior con una pecularidad: Una funcion que retorna otra funcion

def sum_hundred():
    def add(value):
        return value + 100 
    return add
print("Funcion sum_hundred()")
print(sum_hundred()(1))
add_hundred = sum_hundred()
print(add_hundred(1))

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

print("Funcion sum_ten()")    
print(sum_ten(1)(45))

add_closure = sum_ten(1)
print(add_closure(5))

print((sum_ten(5))(1))

### Built-in Higher Order Functions ###

# map()***************************************

numbers = [2, 5, 10, 21, 3, 30]

def multiply_two(number):
    return number * 2

doble_num =list( map( lambda x : x * 2, numbers))
print(doble_num)

multiply_two_numbers = list(map(multiply_two, numbers))
print(multiply_two_numbers)

# Filter **********************************

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False
    

print(list(filter(filter_greater_than_ten, numbers)))

print(list(filter(lambda x: x % 2 == 0, numbers)))

# Reduce()*************************************
# Hay que importarlo del modulo functools

from functools import reduce

def sum_two_values(valor_inicial, acumulado):
    print(valor_inicial)
    print(acumulado)
    return valor_inicial + acumulado

print(reduce(sum_two_values, numbers))
print(reduce(lambda x, y: x + y, numbers))





