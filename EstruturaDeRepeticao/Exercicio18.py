#Exercicio 18: Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
quantidade = int(input("Digite quantos numeros voce irá adicionar: "))
maior = 0
menor = 999999999999999999999999999999999999999999999999
soma = 0

for n in range(1, quantidade + 1, 1):
    numero = int(input("Digite um numero: "))
    soma += numero    
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("Maior numero:", maior)
print("Menor numero:", menor)
print("Soma entre todos:", soma)