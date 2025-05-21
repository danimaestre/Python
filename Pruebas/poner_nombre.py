class PonerNombre:
    def __init__(self, nombre, ciudad, anio):
        self.nombre = nombre
        self.ciudad = ciudad
        self.anio = anio
        self.RepiteNombre()
        self.infomation()
        self.imprimirLogo()
        
    def RepiteNombre(self):
        for i in range (5):
            print(self.nombre)
            
    def infomation(self):
        print(f'{self.nombre} vive en {self.ciudad}\ntiene {self.anio} años')
        
    def __str__(self):
        return f'Nombre: {self.nombre}, Ciudad: {self.ciudad}, Edad: {self.anio}'
    
    def imprimirLogo(self):
        for i in range(4):
            for j in range(4):
                print('*  ', end="")
            print()
            
nombre = PonerNombre('Daniel', 'Paraguay', 67)
nombre2 = PonerNombre('Juan', 'Alemania', 25)
#nombre.imprimirLogo()

'''************************************************************'''

empleados = [nombre, nombre2]
for nombre in empleados:
    print(nombre)
    
#***************************************************************


