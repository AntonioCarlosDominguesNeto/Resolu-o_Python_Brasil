#Exercicio 10: Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
vetor1 = []
vetor2 = []
vetor3 = []

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

for n in range(1, 21, 1):
    if (n - 1) % 2 == 0:
        vetor3.append(int(vetor1[contador]))
    else:
        vetor3.append(int(vetor2[contador]))
    calculo3 = vetor3[n - 1] ** 2
    print("Valor recebido:", vetor3[n - 1])
    print("Elevado ao quadrado:", calculo3)
    contador += 1
    if contador == 9:
        contador = 0