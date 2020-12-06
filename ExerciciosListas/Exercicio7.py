#Exercicio 7: Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
numeros = []
contador = 1
multiplicacao = 1

while contador != 6:
    numeros.append(int(input("Digite um numero: ")))
    multiplicacao *= numeros[contador - 1]
    contador += 1

soma = sum(numeros)

print("Numeros adicionados:", numeros)
print("A soma de todos os numeros:", soma)
print("A multiplicação de todos os numeros", multiplicacao) 