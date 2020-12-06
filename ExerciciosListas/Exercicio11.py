#Exercicio 11: Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

for n in range(1, 11, 1):
    vetor1.append(int(input("Digite o vetor: ")))
    calculo1 = vetor1[n - 1] ** 2
    print("Elevado ao quadrado fica:", calculo1)

print("\n")

for n in range(1, 11, 1):
    vetor2.append(int(input("Digite o vetor: ")))
    calculo2 = vetor2[n - 1] ** 2
    print("Elevado ao quadrado fica:", calculo2)

print("\n")
contador = 0

for n in range(1, 11, 1):
    vetor3.append(int(input("Digite o vetor: ")))
    calculo3 = vetor3[n - 1] ** 2
    print("Elevado ao quadrado fica:", calculo3)

print("\n")

for n in range(1, 21, 1):
    if n == 0 or n == 3 or n == 6 or n == 9 or n == 12 or n == 15 or n == 18 or n == 21 or n == 24 or n == 27:
        vetor4.append(int(vetor1[contador]))
    elif n == 1 or n == 4 or n == 7 or n == 10 or n == 13 or n == 16 or n == 19 or n == 22 or n == 25 or n == 28:
        vetor4.append(int(vetor2[contador]))
    else:
        vetor4.append(int(vetor3[contador]))
    calculo4 = vetor4[n - 1] ** 2
    print("Valor recebido:", vetor4[n - 1])
    print("Elevado ao quadrado:", calculo4)
    contador += 1
    if contador == 9:
        contador = 0