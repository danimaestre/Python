def diccionario(**kwargs):
    print(kwargs)
    
diccionario(nombre = "Daniel", apellido = "Maestre", edad = 55)

def datos(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)
    
usuario1 = {"nombre": "Gabriela",
            "apellidos": "Roman Martin",
            "edad" : 34}

datos("hola", 56.78, "Redondo", **usuario1)