'''
Exercicio 12: Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS
corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido 
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
Desconto do IR: 
 ° Salário Bruto até 900 (inclusive) - isento
 ° Salário Bruto até 1500 (inclusive) - desconto de 5%
 ° Salário Bruto até 2500 (inclusive) - desconto de 10%
 ° Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
 abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''
salarioHora = float(input("Digite quanto você ganha por hora trabalhada: R$"))
quantidadeHora = int(input("Digite quantas horas você trabalha por mês: "))
salarioBruto = salarioHora * quantidadeHora
descontoSindicato = salarioBruto * 0.03

if salarioBruto <= 900:
    descontoIr = salarioBruto * 0
elif salarioBruto <= 1500:
    descontoIr = salarioBruto * 0.05
elif salarioBruto <= 2500:
    descontoIr = salarioBruto * 0.10
else:
    descontoIr = salarioBruto * 0.20

descontos = descontoSindicato + descontoIr
salarioLiquido = salarioBruto - descontos

print("Salário bruto: R$", salarioBruto)
print("Desconto do sindicato: R$", descontoSindicato)
print("Desconto do imposto de renda: R$", descontoIr)
print("Salário liquido: R$", salarioLiquido)