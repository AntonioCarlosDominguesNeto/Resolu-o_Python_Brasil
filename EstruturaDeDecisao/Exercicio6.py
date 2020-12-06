#Exercicio 6: Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
maior = 0

if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print("O maior numero foi:", maior)
