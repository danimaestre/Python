
bandera = False

while not bandera:
    contrasena = input("Introduzca la contraseña, (minimo 8 caracteres)\n")
    if  len(contrasena) >= 8:
        print(f"Contraseña establecida: {contrasena}")
        bandera = True
    else:
        print(f"Error: La contraseña debe tener al menos 8 caracteres. La contraseña {contrasena} tiene {len(contrasena)} caracteres")
     

# *************** Validacion de rango multiple *******************

bandera2 = False

while not bandera2:
    try:
        numero = int(input("Introduce un numero del 1 al 10: "))
        if numero > 0 and numero < 11:
            bandera2 = True
        else:
            print("He dicho entre 1 y 10")
            
            
    except:
        print("Ese no es un valor valido")
        
print(f"El numero introducido es: {numero}")