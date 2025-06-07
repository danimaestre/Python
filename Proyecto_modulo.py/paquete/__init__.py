import paquete.modulo1, paquete.modulo2 ,paquete.subpaquete.modulo3, paquete.subpaquete.modulo4

'''
    Esto es para poder importar todos los modulos de un paquete con el * (principal.py --> from paquete import *):
        __all__ = ["modulo1", "modulo2"]

'''


print(f"El paquete llamado '{__name__}' ha sido inicializado fuera de la zona restringida")

def descripcion():
    print("Soy el paquete")
    
if __name__ == "__main__":
    print("Ejecutado desde mi propio archivo")
    print(__name__)
    
