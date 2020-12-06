#Desafio 22: Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
n = int(input("Digite um numero: "))
if n / 2 % 1:
    print("O numero", n, "é: Impar")
else:
    print("O numero", n, "é: Par")