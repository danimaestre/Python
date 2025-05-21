### Desafios (Challenges) ###

'''
Escribe un programa que muestre por consola (CON UN PRINT) los numeros del 1 a 100 (ambos inclusive y con un salto de linea en cada impresion), sustituyendo los siguientes:
    *Multiplos de 3 por la palabra "fizz"
    *Multiplos de 5 por la palabra "buzz"
    *Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"

'''

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(str(i) + ": fizzbuzz")
        elif i % 5 == 0:
            print(str(i) + ": buzz")
        elif i % 3 == 0 :
            print(str(i) + ": fizz")
        else:
            print(i)
            
fizzbuzz()

'''
Escribe una funcion que reciba 2 palabras (strings) y retorne verdadero o falso (bool) segun sean o no anagramas.
    -Un anagrama consiste en formar una palabra reoordenando todas las letras de otra palabra inicial.
    -No hace falta comprobar que ambas palabras existan.
    -Dos palabras exactamente iguales no son anagramas
'''

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        print("No es un Anagrama, pues las palabras son iguales")
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())
    
print(is_anagram("hola","hola"))
print(sorted('hola'))
print("".join(sorted('hola')))

'''
Escribe un programa que imprima la sucesion de fiboacci de los primeros 50 numeros empezando en 0.
    0,1,1,2,3,5,8,13......
'''

def sucesion_fibonacci(num):
    x = 0
    y = 1
    
    
    for _ in range(0,num+1):
        
        z = x + y
        x = y
        y = z
        print(z, end=", ")
        
sucesion_fibonacci(10)
print('******************************************************')

'''
Escribe un programa que se encarge de determinar si un numero es primo o no. Hecho esto escribe los numeros primos entre 1 y 100.
'''

def is_prime():
    
    for number in range(1, 101):
        if number >= 2:
            is_divisible = False
            for i in range (2, number):
                if number % i == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)
        

is_prime()

'''
Crea un programa que invierta cadenas sin usar funciones propias del lenguaje que las inviertan de forma automatica.
'''

def cadena_invertida(cadena):
    cadena_invertida = cadena[::-1]
    print(cadena_invertida)
    
cadena_invertida('Daniel')

def reverse(text):
    reversed_text = ""
    for letra in range(0, len(text)):
        reversed_text += text[len(text)-1 - letra]
    return reversed_text

print(reverse('Hola mundo'))
    
    
