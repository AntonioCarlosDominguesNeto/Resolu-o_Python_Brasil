#Exercicio 8: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganhaHora = float(input("Digite o quanto você ganha por hora trabalhada: "))
tempoHora = int(input("Digite quantas horas você trabalha por mês: "))
salario = ganhaHora * tempoHora

print("Seu salário é de:", salario)