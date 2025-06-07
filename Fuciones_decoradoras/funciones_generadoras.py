'''
    La funcion generadora permite la creacion de un objeto iterador que se puede ejecutar paso por paso, en lugar de todo a la vez. Se dice que estas funciones son de evaluacion diferiida porque se van ejecutando de manera gradual generando un valor a la vez y no todos de golpe. Solo se ejecuta cuando se solicite el primer valor mediante la funcion next() o al usar el generador con un bucle for. Divide una ejecucion de funcion en partes mas pequeñas para aprovechar mejor los recursos del sistema en terminos de memoria.
    
    La palabra reservada yield es parecida a return con una diferencia: una funcion con return o print se ejecuta integra al momento de la llamada, procesan todos los datos de una sola vez se convierte en un problema al trabajar con una cantidad grande de datos. Yield devuelve valores por pasos como un bucle y su iteraciones

'''

def generadora():
    for i in range(10):
        print(i, end=", ")
    
generadora()

def generadora_numeros():
    lista_valores = []
    for i in range(0,15):
        lista_valores.append(i)
    return lista_valores

valores = generadora_numeros()
print("\n",valores)

# ********* Funcion generadoras ***********


# Crea objeto iterador esperando ser iterada, al momento de llamar a la funcion <generator object generadora2 at 0x0000020AA5476740>
# Gracias a yield vamos pausando y llamando la ejecucion de la funcion
def generadora2():
    for i in range(10):
        yield i
        
rango = generadora2()
print(next(rango))
print(next(rango))
print("Acciones independientes de la funcion")
print(next(rango))
print(next(rango))
print(next(rango))
print(next(rango))

# *********** Utilizar varios yield en la misma funcion ***********
  # return finaliza funcion, yield no
def generadora3():
    for i in range(0, 10):
        if i % 2 == 0:
            yield f"{i} -par"
        else:
            yield f"{i} -impar"
            
rango3 = generadora3()

print("--------------")
print(next(rango3))
print(next(rango3))
print(next(rango3))
print(next(rango3))

'''
  --Un "objeto generador o iterador " se crea utilizando una funcion generadora mediante la palabra clave yield, si utilizamos esta palabra clave en una funcion de python generamos un objeto generador o iterador. Los generadores crean elementos sobe la marcha y no almacenan toda la secuencia en la memoria de golpe, gracias a esto son eficientes para maneja grandes cantidades de datos al poder hacerlo de manera dosificada por partes a medida que esoos datos se van necesitando o con unas pasas determinadas. 
  --Un "objeto iterable" es cualquier objeto que se puede iterar mediante un bucle, como una lista, cadena, tupla, un set, ect.
  Diferencias clave: El generador se crea a traves de una funcion generadora utilizando yield, un "iterable" se crea mediante estructuras de datos como pueden ser --> listas, tuplas, strings, sets ... El generador crea cada elemento sobre la marcha y no almacena los elementos en memoria, el iterable almacena todos los elementos en memoria. El generador una vez que se crea el elemento no se puede volver a generar, no se puede volver atras, hay que seguir adelante hasta que se termine de recorrer y una vez se termina se tiene que volver a generar, crear otro objeto generador para volver a utilizarlo.
  Un iterable lo podemos acceder multiples veces, podemos rrecorrer una lista arriba a bajo ir posicion 0 y volver a hacerlo en cualquier momento.
  El generador mantiene su estado a cada llamada cada vez que utilizamos next se pausa y seguimos mas adelante pero el estado, la posicion del objeto generador queda ahi en espera hasta que ejecutemos otra parte mas. Nos permite retomar la ejecucion justa despues de la ultima llamada. Y el iterable no mantenes estados entre iteraciones. Cada iteracion empieza desde 0 

''' 

# funcion iter() nos permite crear objetos iteradores a partir de iterables

# iterable
cadena = "hola"

cadena_generador = iter(cadena)
print(type(cadena_generador))

print(next(cadena_generador))
print(next(cadena_generador))
print(next(cadena_generador))

# Convierte objeto iterador en iterable

def generadora4():
    for i in range(0, 10):
        if i % 2 == 0:
            yield f"{i} -par"
        else:
            yield f"{i} -impar"
            
rango4 = generadora4()
lista_generador = list(rango4)
print(lista_generador)
print(lista_generador[2])
print(lista_generador[7])

# excepcition stopiteration

def generadora5():
    for i in range(0, 3):
        yield i
        
rango5 = generadora5()
try:
    print(next(rango5))
    print(next(rango5))
    print(next(rango5))
    print(next(rango5)) #--> se sale del rango: StopIteration
except StopIteration:
    print("La ejecucion finalizo")            