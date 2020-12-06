#Exercicio 15: A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo
numero = int(input("Digite o numero da sequencia que deseja saber: "))
termo1 = 0
termo2 = 1
resposta = 0

for n in range(1, numero + 1, 1):
    termo3 = termo2 + termo1
    termo1, termo2 = termo2, termo3
    print(termo2)