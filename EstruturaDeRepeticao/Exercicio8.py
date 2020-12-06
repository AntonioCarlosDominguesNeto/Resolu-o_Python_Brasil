#Exercicio 8: Faça um programa que leia 5 números e informe a soma e a média dos números.
contador = 0 
soma = 0

while contador <=4:
    numero = int(input("Digite um numero: "))
    soma += numero
    contador += 1

resultado = soma / 5
print("O resultado é:", resultado)