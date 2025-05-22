### Error Types ###

# SyntaxError

# print "Hola mundo" # Descomentar para error
print("hola Mundo")

# NameError

language = "spanish" # Comentar para error
print(language)

# IndexError

my_list = ['Python', 'Kotlin', 'Swift', 'Dart', 'JavaScript']
print(my_list[4])
#print(my_list[5]) # Descomentar para error

# ModuleNotFoundError

# import maths # Descomentar para error
import math

# AttributeError

#print(math.Pi) # Descomentar para error
print(math.pi)

# KeyError

my_dict = {'Nombre':'Brais', 'Apellido': 'Moure', 'Edad': 34, 1:'Phyton'}
#print(my_dict['name']) # Descomentar para error
print(my_dict['Edad'])

# TypeError

#print(my_list["Nombre"]) # Descomentar para error
print(my_list[0])

# ImportError

#from math import pii # Descomentar para error
from math import pi

# ValueError

my_int = int('10')
#my_int = int("10 Años") # Descomentar para error
print(my_int)
print(type(my_int))

# ZeroDivisionError

#print(12/0) # Descomentar para error
print(4/2)



