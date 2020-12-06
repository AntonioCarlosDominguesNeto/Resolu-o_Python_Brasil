'''
Exercicio 16: Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em 
comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, 
um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um 
total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam 
salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
'''
salario = 200
quantidade1 = 0
quantidade2 = 0
quantidade3 = 0
quantidade4 = 0
quantidade5 = 0
quantidade6 = 0
quantidade7 = 0
quantidade8 = 0
quantidade9 = 0

for n in range(1, 11, 1):
    vendas = float(input('Informe o valor das vendas do vendedor: '))
    salarioFinal = vendas * 0.09 + salario
    if salarioFinal >= 200 and salarioFinal <= 299:
        quantidade1 += 1
    elif salarioFinal >= 300 and salarioFinal <= 399:
        quantidade2 += 1
    elif salarioFinal >= 400 and salarioFinal <= 499:
        quantidade3 += 1
    elif salarioFinal >= 500 and salarioFinal <= 599:
        quantidade4 += 1
    elif salarioFinal >= 600 and salarioFinal <= 699:
        quantidade5 += 1
    elif salarioFinal >= 700 and salarioFinal <= 799:
        quantidade6 += 1
    elif salarioFinal >= 800 and salarioFinal <= 899:
        quantidade7 += 1
    elif salarioFinal >= 900 and salarioFinal <= 999:
        quantidade8 += 1
    elif salarioFinal >= 1000:
        quantidade9 += 1
    else:
        print("Salário invalido!")

print("\n")
print("Salários entre 200 e 299:", quantidade1)
print("Salários entre 300 e 399:", quantidade2)
print("Salários entre 400 e 499:", quantidade3)
print("Salários entre 500 e 599:", quantidade4)
print("Salários entre 600 e 699:", quantidade5)
print("Salários entre 700 e 799:", quantidade6)
print("Salários entre 800 e 899:", quantidade7)
print("Salários entre 900 e 999:", quantidade8)
print("Salários de 1000 em diante:", quantidade9)