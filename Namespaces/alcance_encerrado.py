'''
    Alcance encerrado hace que una funcion anidada(hija) acceda a las variables de la funcion que la contiene funcion(padre).
    
    La palabra reservada NonLocal se usa para trabajar con variables dentro de funciones anidadas donde la variable no debe pertenecer a la funcon interna

'''

def funcion_externa():
    a = 10
    def funcion_interna():
        b = 20
        print(a, b)
    funcion_interna()
    
funcion_externa()

def funcion_externa_2(): # --> a, a son dos variables distintas por encontrarse en distintos ambito de alcance
    a = 10
    def funcion_interna():
        nonlocal a # --> Ahora se reasigna valor a = 100 a=a
        a = 100
        print(a)
        
    funcion_interna()
    print(a)
    
funcion_externa_2()

def funcion_externa_3():
    a = 10
    def funcion_interna():
        # nonlocal b --> error porque b no existe funcion padre
        b = 100
        
    funcion_interna()
    
# Para acceder al diccionario de espacio cerrado

def funcion_externa6():
    a = 10
    print(f"Alcance local: {locals()}")
    
    def funcion_interna():
        a = 100
        print(f"Alcance encerrado: {locals()}")
        
    funcion_interna()
    
funcion_externa6()