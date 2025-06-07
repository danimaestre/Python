"""
    Podemos importar un paquete entero pero para que funcione hemos de dotar al paquete del archivo __init__.py vacio para
    que el interprete de python lo considere un modulo y no una carpeta normal . ¡ No se puede llamar al paquete solo, la forma correcta es: ==> import paquete.modulo1, paquete.subpaquete.modulo3. Mejor inicializarlo directamente desde archivo __init__.py


"""

#import paquete.modulo1, paquete.subpaquete.modulo3, paquete.subpaquete.modulo4  # inicializado desde init

import paquete

paquete.modulo1.descripcion()
paquete.modulo2.descripcion()
paquete.subpaquete.modulo3.descripcion()
paquete.subpaquete.modulo4.descripcion()


paquete.descripcion()# accede solo al modulo __init__.py

