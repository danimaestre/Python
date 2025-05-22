### Exceptions Handling ###

numberOne = 5
numberTwo = '1'
#numberTwo = 1

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
    
# try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepcion
    print('La ejecucion continua correctamente')
finally:
    # Se ejecuta siempre haya o no excepcion
    print('La ejecucion contina')
    
# Excepciones por Tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:  #-->  solo captura ValueError 
    print("Se ha producido un ValueError")
except TypeError:  #-->  solo captura TypeError 
    print("Se ha producido un TypeError")
    
# Captura de la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:  
    print(f'Se ha producido un error: {error}')
except Exception as error:
    print(f'Se ha producido un error: {error}')