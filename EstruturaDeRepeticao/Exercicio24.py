#Exercicio 24: Faça um programa que calcule o mostre a média aritmética de N notas.
quantidadeNota = int(input("Digite quantas notas serão publicadas: "))
contador = 0
soma = 0

while contador < quantidadeNota + 1:
    nota = float(input("Digite a nota: "))
    soma += nota
    contador += 1

resultado = soma / quantidadeNota
print("A média foi:", resultado)