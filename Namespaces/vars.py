class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
usuario1 = Usuario("Enrique", "Barros", 32)
usuario2 = Usuario("Elvira", "Fernandez", 28)

# Definicion de un atributo difernte a cada objeto
usuario1.correo = "correo@gmail.com"
usuario2.telefono = "123456789"

print(usuario1.__dict__)
print(vars(usuario2)) # --> mas facil vars()