#Exercicio 27: Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
numeroTurmas = int(input("Digite quantas turmas: "))
soma = 0
contador = 0

while contador < numeroTurmas:
    numeroAlunos = int(input("digite quantos alunos têm na turma: "))
    if numeroAlunos > 0 and numeroAlunos <= 40:
        soma += numeroAlunos
        contador += 1
    else:
        print("Quantidade invalida!")

media = soma / numeroTurmas 

print("Média de alunos por turma:", media)