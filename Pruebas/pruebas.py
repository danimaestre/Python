

datos = {
    "Angel": 72,
    "Antoñio": 80,
    "Mary": 82,
    "Dañiel": 78
    }

for nombre, edad in datos.items():
    print(f"Nombre: {nombre}, Edad: {edad}")

nombres = []
edades = []

for dato in datos.keys():
    nombres.append(dato)

print(nombres)

for edad in datos.values():
    edades.append(edad)

print(edades)

print("----------------------------------------------------")

def suma_regresiva(n):
    
    if n < 0:
        print("FIN")
    else:
        print(n, end=",")
        
        suma_regresiva(n-1)
    

suma_regresiva(30)

def cuenta_adelante(m,n):
    if m == n:
        print("FIN")
    else:
        print(m, end="-")
        cuenta_adelante(m+1, n)

cuenta_adelante(6,20)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sumar_lista(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + sumar_lista(lista[1:])

print(sumar_lista(numeros))


    
