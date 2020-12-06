#Exercicio 7: Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
maior = 0
menor = 99999999999999999999

if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n1 < menor:
    menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print("O maior numero foi:", maior)
print("O menor numero foi:", menor)