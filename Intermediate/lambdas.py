### Funciones lambda (funciones anonimas) ###

sum_two_values = lambda first_value, second_value : first_value + second_value

print(sum_two_values(45,78))

multiply_values = lambda first_value, second_value : first_value * second_value - 3

print(multiply_values(20,6))

def sum_three_values(values):
    return lambda  first_value, second_value : first_value + second_value + values


print(sum_three_values(4)(5,8))
