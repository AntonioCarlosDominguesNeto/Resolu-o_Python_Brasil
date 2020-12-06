#Exercicio 7: Faça um programa que leia 5 números e informe o maior número.
contador  = 0
maior = 0

while contador <= 4:
    numero = int(input("Digite um numero: "))
    if numero > maior:
        maior = numero
    contador += 1

print("O maior numero foi:", maior)