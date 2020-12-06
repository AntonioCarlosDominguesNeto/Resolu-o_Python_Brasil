#Exercicio 6: Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
notaFinal = []
contador = 0

while contador != 10:
    soma = 0
    for n in range(1, 5, 1):
        nota = float(input("Digite a nota: "))
        soma += nota
    
    media = round(soma / 4)
    notaFinal.append(media)
    
    quantidade = 0
    for q in notaFinal:
        if q >= 7:
            quantidade +=1
    
    print("\n")
    contador += 1

print("Média dos alunos:", notaFinal)
print("Quantidade de alunos com notas maiores ou igual a 7:", quantidade)