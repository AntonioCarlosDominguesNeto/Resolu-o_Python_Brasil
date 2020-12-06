'''
Exercicio 14:
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
A. "Telefonou para a vítima?"
B. "Esteve no local do crime?"
C. "Mora perto da vítima?"
D. "Devia para a vítima?"
E. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa 
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 
4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
soma = 0

pergunta1 = str(input("Telefonou para vitima[S/N]:")).upper().split()[0]
if pergunta1 in "S":
    soma += 1

pergunta2 = str(input("Esteve no local do crime[S/N]:")).upper().split()[0]
if pergunta2 in "S":
    soma += 1

pergunta3 = str(input("Mora perto da vitima[S/N]:")).upper().split()[0]
if pergunta3 in "S":
    soma += 1

pergunta4 = str(input("Devia para vitima[S/N]:")).upper().split()[0]
if pergunta4 in "S":
    soma += 1

pergunta5 = str(input("Já trabalhou com a vitima[S/N]:")).upper().split()[0]
if pergunta5 in "S":
    soma += 1

if soma < 2:
    print("Inocente!")
elif soma == 2:
    print("Suspeita!")
elif soma == 3 or soma == 4:
    print("Cumplice")
elif soma == 5:
    print("Assassino!")
else:
    print("Caractere invalido!")