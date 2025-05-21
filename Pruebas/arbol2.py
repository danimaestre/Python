import random

class Arbol:
    def __init__(self, altura: int, figura: str):
        self.altura = altura
        self.base = 2 * altura - 1
        self.figura = figura
        self.espacios = " "

    def dibujar_arbol(self):
        espacios_iniciales = self.base // 2

        for i in range(1, self.base + 1, 2):
            print(self.espacios * espacios_iniciales, end='')
            
            # Agregar decoraciones aleatorias
            fila = [random.choice([self.figura, "*", "o"]) for _ in range(i)]
            print("".join(fila))
            
            espacios_iniciales -= 1
        
        # Agregar tronco
        for i in range(4):
            print(self.espacios * (self.base // 2) + "|||")
        


print('*******************************************************')
print()

figura1 = Arbol(11, "+")
figura1.dibujar_arbol()
