#Exercicio 34: Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
numero = int(input("Digite um numero: "))
contadorDivisao = 0

for n in range(1, 10, 1):
    if numero % n == 0:
        contadorDivisao += 1

if contadorDivisao == 2:
    print("O numero", numero, "é primo!")
else:
    print("O numero", numero, "não é primo!")