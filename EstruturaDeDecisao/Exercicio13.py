#Exercicio 13: Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
numeroSemana = int(input("Digite um numero correpondente a semana: "))
diaSemana = "Numero inválido!"

if numeroSemana == 1:
    diaSemana = "Domingo"
elif numeroSemana == 2:
    diaSemana = "Segunda-Feira"
elif numeroSemana == 3:
    diaSemana = "Terça-Feira"
elif numeroSemana == 4:
    diaSemana = "Quarta-Feira"
elif numeroSemana == 5:
    diaSemana = "Quinta-Feira"
elif numeroSemana == 6:
    diaSemana = "Sexta-Feira"
elif numeroSemana == 7:
    diaSemana = "Sabado"
else:
    print("Numero inválido!")

print("Dia correspondente ao numero:", diaSemana)