#Exercicio 2: Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
numeros = []
for n in range(1, 11, 1):
    numeros.append(int(input("Digite um numero: ")))
numeros.reverse()
print("Numeros digitados em ordem reversa:", numeros)