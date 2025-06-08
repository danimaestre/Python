'''
    En python no hay alcance de bloque como ocurre en javascrip, que una variable solo sea accesible en el bloque que se declaclara... if, condicional etc. En python estas variables son globales

'''

if True:
    nombre = "Variable declarada" # --> alcance global
    
print(nombre)