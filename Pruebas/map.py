numeros:list = [5, 8, 2, 22, 57, 66, 71, 78]

numeros_pares = list(filter(lambda num: num % 2 == 0, numeros))

numeros_cuadrado = list(map(lambda num: num**3, numeros))

print(numeros_pares)
print(numeros_cuadrado)

nombres = ["Luis", "Daniel", "Roberto", "Angel"]

nombres_l = list(filter(lambda nombre: nombre.lower().startswith("r"), nombres))

nombres_4 = list(filter(lambda nombre: len(nombre) <=5, nombres))

print(nombres_l)
print(nombres_4)

for clave, valor in enumerate(nombres, 1):
    print(f"{clave}: {valor}")
    
num_par = [num for num in range(1, 25) if num % 2 == 0 ]

num_impar = [num if num % 2 == 0 else "X" for num in range(0, 25,3) ]

print(num_par)

print(num_impar)