#Exercicio 9: Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
vetor = []

for n in range(1, 11, 1):
    vetor.append(int(input("Digite o vetor: ")))
    calculo = vetor[n - 1] ** 2
    print("Elevado ao quadrado fica:", calculo)