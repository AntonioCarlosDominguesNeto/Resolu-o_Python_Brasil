'''
Exercicio 38: Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
A. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
B. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
C. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano 
anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o 
programa permitindo que o usuário digite o salário inicial do funcionário
'''
salarioInicial = 1000
aumento1996 = salarioInicial * 0.015
salario1997 = salarioInicial + aumento1996
ano = 1997
aumento1997 = 0.03
aumentoFinal = 0

for n in range(1, 24, 1):
    aumentoFinal += aumento1997 * 2

salarioFinal = salario1997 * aumentoFinal 
print("Salário final:", salarioFinal)