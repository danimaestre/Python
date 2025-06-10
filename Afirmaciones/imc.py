
def calcular_imc(peso, altura):
    assert peso > 0, "El peso debe ser mayor que 0"
    assert altura > 0, "La altura debe ser mayor que 0"
    
    imc = peso / (altura ** 2)
    return imc


#imc1 = calcular_imc(56, 0)
#print (imc1)