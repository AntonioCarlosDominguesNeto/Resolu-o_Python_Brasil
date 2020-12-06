'''
Exercicio 45: Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa 
deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular 
o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser 
feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
A. Maior e Menor Acerto;
B. Total de Alunos que utilizaram o sistema;
C. A Média das Notas da Turma.
'''
reposta1 = "A"
reposta2 = "B"
reposta3 = "C"
reposta4 = "D"
reposta5 = "E"
reposta6 = "E"
reposta7 = "D"
reposta8 = "C"
reposta9 = "B"
reposta10 = "A"
acertos = 0
erros = 0
contador = 0
totalAlunos = 0
soma = 0
maior = 0
menor = 999999999999999999999999999999999999999

while True:
    if contador == 0:
        continuar = str(input("Digite se tem mais um aluno[S/N]: ")).upper().split()[0]
        if continuar in "S":
            totalAlunos += 1
            contador += 1
        else:
            break
    else:
        pergunta = str(input("Digite a resposta: ")).upper().split()[0]        
        if contador == 1:
            if pergunta in "A":
                acertos += 1
            else:
                erros += 1
        elif contador == 2:
            if pergunta in "B":
                acertos += 1
            else:
                erros += 1
        elif contador == 3:
            if pergunta in "C":
                acertos += 1
            else:
                erros += 1
        elif contador == 4:
            if pergunta in "D":
                acertos += 1
            else:
                erros += 1
        elif contador == 5:
            if pergunta in "E":
                acertos += 1
            else:
                erros += 1
        elif contador == 6:
            if pergunta in "E":
                acertos += 1
            else:
                erros += 1
        elif contador == 7:
            if pergunta in "D":
                acertos += 1
            else:
                erros += 1
        elif contador == 8:
            if pergunta in "C":
                acertos += 1
            else:
                erros += 1
        elif contador == 9:
            if pergunta in "B":
                acertos += 1
            else:
                erros += 1
        elif contador == 10:
            if pergunta in "A":
                acertos += 1
            else:
                erros += 1
        elif contador > 10:
            contador = -1
            soma = 0
        soma += acertos
        
        if soma > maior:
            maior = soma
        if soma < menor:
            menor = soma
        
        contador += 1
    
print("Pontos ganhos:", acertos)
print("Alunos que fizeram a prova:", totalAlunos)
print("Maior nota", maior)
print("Menor nota", menor)