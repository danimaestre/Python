'''
    Esta por encima del ambito global tiene un conjunto de nombres que esta predefinido en cualquier programa python sin la necesidad de importar ningun modulo ni hacer referencias explicitas en el propio modulo 

'''
# Acceder a este espacio de nombres:

print(__builtins__.__dict__)
#print(vars(__builtins__)) #Otra forma de acceder