argumentos = {"Nombre": "Enrique",
              "Edad": 32,
              "Telefono": "123456789"}

print(type(argumentos.items()))
print(argumentos.items())

def info(**kwars):
    for clave, valor in kwars.items():
        print(f"Clave: {clave}, Valor: {valor}")
        
info(**argumentos)