
bandera = False

while not bandera:
    try:
        numero = int(input("Introduce un número: "))
        print(f"El número elegido es: {numero}")
        bandera = True
    except ValueError:
        print("Debe ser un número entero, vuelva a intentarlo.")
