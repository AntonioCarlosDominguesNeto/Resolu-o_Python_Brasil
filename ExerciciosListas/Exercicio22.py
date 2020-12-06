tipoProblema = [0] * 4
contador = 0

while True:
    tipo = int(input('Digite a identificação: '))
    if tipo < 0 or tipo == 0:
        break
    problema = int(input('Digite o problema: '))
    tipoProblema[problema - 1] = tipoProblema[problema - 1] + 1
    contador += 1

print("Tipos de problemas:")
print("\n")
print("Quantidade:", contador)
print("Esfera:", tipoProblema[0])
print("Limpeza:", tipoProblema[1])
print("Cabo ou conector:", tipoProblema[2])
print("Inutilizado:", tipoProblema[3])