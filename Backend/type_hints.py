### Type hints ###

my_string_variable = "Mi string variable"
print(type(my_string_variable))
print(my_string_variable)

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

# Especificar tipo de dato, aunque no se puede obligar a tipar porque python es de tipado debil. (Buena practica para programar en backend...)

my_typed_variable: str = "My typed String variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))
