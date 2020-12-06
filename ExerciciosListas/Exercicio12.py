#Exercicio 12: Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
idadeFinal = []
alturaFinal = []
contador = 0

while contador != 30:
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    idadeFinal.append(idade)
    alturaFinal.append(altura)
    print("\n")
    contador += 1

media = sum(alturaFinal) / 30
quantidade = 0

for n in range(1, 31, 1):
    if idadeFinal[n - 1] >= 13 or alturaFinal[n - 1] >= media:
        pass
    else:
        quantidade += 1

print("Alunos menores de 13 anos abaixo da média de altura:", quantidade) 