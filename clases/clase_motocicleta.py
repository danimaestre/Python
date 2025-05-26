class Motocicleta():
    estado = "nueva"
    motor = False
    
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, combustible_maximo, precio = "'No asignado'"):
        self.color = color
        self.matricula = matricula
        self. combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.veloocidad_punta = velocidad_punta
        self.peso = peso
        self.combustible_maximo = combustible_maximo
        self.precio = precio
        
    def arrancar(self):
        if self.motor:
            print("Se escucha un  ruido raro al girar la llave, el motor esta encendido")
        else:
            print(f"Se ha arrancado el motor de {self.marca}. Ruge como un leon")
            
    def detener(self):
        if self.motor:
            print("¡¡¡El motor acaba de pararse!!!")
        else:
            print(f"No puedes parar el motor de {self.marca} porque el motor ya esta parado")
            
    def consulta_precio(self):
        print(f"El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio} €")
        
    def comprobar_deposito(self):
        print(f"--->REPORTE DEL DEPOSITO DE {self.marca} {self.modelo}<---")
        print(f"El deposito tiene {self.combustible_litros} litros")
        print(f"La capacidad maxima del tanque de combustible es de {self.combustible_maximo}.")
        print(f"Faltan {self.combustible_maximo - self.combustible_litros} para llenar el deposito.")
        print("--->FIN DEL REPORTE<---\n")
        
    def repostar(self):
        while True:
            self.repostar_litros = float(input("Por favor, introduzca la cantidad de litros que desea repostar\n"))
            
            if self.combustible_litros + self.repostar_litros <= self.combustible_maximo:
                print("Repostaje exitoso")
                print(f"Se ha repostado {self.repostar_litros} litros.")
                self.combustible_litros += self.repostar_litros
                print(f"El deposito tiene {self.combustible_litros} litros de combustible")
                break
            else:
                print("No cabe tanto combustible. ¿Quieres encharcar el concesionario?")
            

#Instancias de la clase motocicletas
motocicleta_yamaha_1 = Motocicleta("Roja y blanca", "45663-FHDY", 10, 2, "Yamaha", "YZF-R1", "20/02/2020", 288, 199, 17)

motocicleta_harley_1 = Motocicleta(
    matricula = "48659-FHEZ",
    combustible_litros = 0,
    color = "Negra",
    marca = "Harley Davidson",
    modelo = "Fat-Boy",
    numero_ruedas = 2,
    peso = 304,
    fecha_fabricacion = "29/09/2020",
    velocidad_punta = 160,
    combustible_maximo = 20
)

motocicleta_yamaha_1.arrancar()
motocicleta_harley_1.detener()

motocicleta_yamaha_1.precio = 23890 

motocicleta_yamaha_1.consulta_precio()
motocicleta_harley_1.consulta_precio()

motocicleta_yamaha_1.comprobar_deposito()
motocicleta_harley_1.comprobar_deposito()

motocicleta_yamaha_1.repostar()
motocicleta_yamaha_1.comprobar_deposito()

