"""
import paquete.modulo1, paquete.modulo2

paquete.modulo1.descripcion()
paquete.modulo2.descripcion()
"""
# Con Alias
"""
import paquete.modulo1 as md1
import paquete.modulo2 as md2
   
md1.descripcion()
md2.descripcion()
"""


"""
from paquete.modulo1 import sumar

operacion = sumar(4, 36)
print(operacion)
"""
import paquete.subpaquete.modulo3 as md3
import paquete.subpaquete.modulo4 as md4

from paquete import *
modulo2.descripcion()

md3.descripcion()
md4.descripcion()
print(dir())