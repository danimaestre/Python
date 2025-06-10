# ********* Con bandera *************

bandera = False

while not bandera:
    edad = input("Introduce tu edad: ")
    if edad.isdigit():
        print(f"Usted tiene {edad} años")
        bandera = True
    else:
        print("Introduzca un numero entero")
        
# ********* Funcion predefinida type() **********

valor = "Python: El poder de los objetos"
#valor = 56

if type(valor) == str:
    print(f"El objeto es una cadena: {type(valor).__name__}")
else:
    print(f"El objeto no es una cadena: {type(valor).__name__}")
    
# ** Funcion predefinida isinstace()  recomendada sobre type() **

# Es una forma mas limpia de hacerlo en Python

valor2 = 10
if isinstance(valor2, int):
    print(f"El objeto es una cadena: {type(valor2).__name__}")
else:
    print(f"El objeto no es una cadena: {type(valor2).__name__}")
