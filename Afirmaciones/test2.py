
import imc

try:
    peso = float(input("Introduce tu peso en Kilogramos: "))
    altura = float(input("Introduce tu altura en metros: "))

    indice_masa_corporal = imc.calcular_imc(peso, altura)
    print(f"Su indice de masa corporal (IMC) es de: {round(indice_masa_corporal, 2)}")

except ValueError:
    print("Error: Ingrese valores validos para peso y altura")