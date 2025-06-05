class Ciudadano:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
        
    def saludar(self):
        print(f"Hola soy {self.nombre}. Mi profesion es {self.profesion}")
        
class Medico(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "medico")
        
class Policia(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "policia")
        
    # sobrescritura de metodos   
    def saludar(self):
        print("En la oscuridad la luz brillara. En la injusticia, la ley prevalecera. Siempre servire y protegere")
        
    def solicitar_refuerzos(self):
        print("A todas las unidades, solicito refuerzos...")
        
persona1 = Ciudadano("Juan", "ingeniero")
persona2 = Medico("Luis")
persona3 = Policia("Maria")

persona1.saludar()
persona2.saludar()
persona3.saludar()
persona3.solicitar_refuerzos()