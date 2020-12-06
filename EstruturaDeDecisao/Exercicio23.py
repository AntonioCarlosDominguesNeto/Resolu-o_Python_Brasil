#Desafio 23: Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
n = float(input("Digite um numero: "))
if n == int(n):
    print("O numero", n, "é um numero real")
else:
    print("O numero", n, "é um numero decimal")