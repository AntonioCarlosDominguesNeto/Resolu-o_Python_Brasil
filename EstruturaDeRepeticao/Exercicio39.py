#Exercicio 39 Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
maior = 0
menor = 99999999999999999999999999999999999999999999
numeroMaior = 0
numeroMenor = 0

for n in range(1, 11, 1):
    numero = int(input("Digite seu numero: "))
    altura = float(input("Digite sua altura: "))
    if altura > maior:
        maior = altura
        numeroMaior = numero
    if altura < menor:
        menor = altura
        numeroMenor = numero
    
print("Maior aluno:", maior)
print("Numero maior aluno:", numeroMaior, "\n")
print("Menor aluno:", menor)
print("Numero menor aluno:", numeroMenor)
