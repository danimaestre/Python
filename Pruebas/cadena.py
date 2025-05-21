import random


animales = ['gato', 'lince', 'zorro', 'cocodrilo', 'lechuza']

palabra = random.choice(animales)

print(palabra)

resultado = list("-" * len(palabra))


while "-" in resultado:
    
    print("".join(resultado))
    letra = input("Introduce una letra: --> ")

    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                resultado[i] = letra
    else:
        print("Esa letra no esta en la palabra")
    
print("¡Felicidades! La palabra era:", palabra)



