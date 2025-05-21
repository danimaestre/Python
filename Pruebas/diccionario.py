
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
def crear_diccionario(personas):
    diccionario = {}
    for persona in personas:
        diccionario[persona.nombre] = persona.edad     
    return diccionario
# Ejemplo de uso
persona1 = Persona("Daniel", 30)
persona2 = Persona("María", 25)
persona3 = Persona("Luis", 40)
 
lista_personas = [persona1, persona2, persona3]
diccionario_resultante = crear_diccionario(lista_personas)
 
print(diccionario_resultante)


