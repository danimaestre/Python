base = 9
espacios = ' '
dibujo = '*'
espacios_iniciales = base // 2

for i in range(1, base + 1 , 2):
    for cont_espacios in range(espacios_iniciales):
        print (espacios, end='')
    espacios_iniciales -= 1
        
    for cont_caracteres in range(i):
        print(dibujo, end='')
    print(espacios)
    
'''
class Arbol:
    def __init__(self, base:int, figura:str):
        self.base = base
        self.figura = figura
        self.espacios = " "
        self.espacios_iniciales = self.base // 2
        self.crearArbol()

    def crearArbol(self):
        for i in range(1, self.base + 1 , 2):
            for cont_espacios in range(self.espacios_iniciales):
                print (self.espacios, end='')
            self.espacios_iniciales -= 1
            
            for cont_caracteres in range(i):
                print(self.figura, end='')
            print(self.espacios)
        
print('*******************************************************')
print()

figura1 = Arbol(5, "+")

figura2 = Arbol(13, '$')

figura3 = Arbol(25, '^')

'''
class Arbol:
    def __init__(self, altura: int, figura: str):
        self.altura = altura
        self.base = 2 * altura - 1
        self.figura = figura
        self.espacios = " "
        
        

    def dibujar_arbol(self):
        self.espacios_iniciales = self.base // 2
        for i in range(1, self.base + 1, 2):
            print(self.espacios * self.espacios_iniciales, end='')
            print(self.figura * i)
            self.espacios_iniciales -= 1

print('*******************************************************')
print()

figura1 = Arbol(25, "+")
figura1.dibujar_arbol()




    