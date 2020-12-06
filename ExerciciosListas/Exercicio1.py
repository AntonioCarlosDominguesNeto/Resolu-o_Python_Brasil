#Exercicio 1: Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
numeros = []
for n in range(1, 6, 1):
    numeros.append(int(input("Digite um numero: ")))
print("Numeros digitados:", numeros)