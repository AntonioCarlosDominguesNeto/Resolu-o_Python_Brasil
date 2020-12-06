'''
Exercicio 25: Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
A. "Telefonou para a vítima?"
B. "Esteve no local do crime?"
C. "Mora perto da vítima?"
D. "Devia para a vítima?"
E. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
pergunta1 = str(input("Digite se você telefonou para a vitima[S/N]: ")).upper().split()[0]
pergunta2 = str(input("Digite se você esteve no local do crime[S/N]: ")).upper().split()[0]
pergunta3 = str(input("Digite se você mora perto da vitima[S/N]: ")).upper().split()[0]
pergunta4 = str(input("Digite se você devia para a vitima[S/N]: ")).upper().split()[0]
pergunta5 = str(input("Digite se você já trabalho com a vitima[S/N]: ")).upper().split()[0]
pontos = 0

if pergunta1 in "S":
    pontos += 1 
if pergunta2 in "S":
    pontos += 1
if pergunta3 in "S":
    pontos += 1
if pergunta4 in "S":
    pontos += 1
if pergunta5 in "S":
    pontos += 1

print("Quantidade de pontos:", pontos)

if pontos == 2:
    print("Você é: Suspeito")
elif pontos == 3 or pontos == 4:
    print("Você é: Cumplice")
elif pontos == 5:
    print("Você é: Assasssino")
else:
    print("Você é: Inocente")