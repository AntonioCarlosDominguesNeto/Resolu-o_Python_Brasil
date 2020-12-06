'''
Exercicio 15: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de 
Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
A. salário bruto.
B. quanto pagou ao INSS.
C. quanto pagou ao sindicato.
D. o salário líquido.
E. calcule os descontos e o salário líquido:
'''
ganhaHora = float(input("Digite o quanto você ganha por hora trabalhada: "))
tempoHora = int(input("Digite quantas horas você trabalha por mês: "))
salarioBruto = ganhaHora * tempoHora
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
impostoRenda = salarioBruto * 0.11
descontos = inss + sindicato + impostoRenda
salarioLiquido = salarioBruto - (inss + sindicato + impostoRenda)

print("Salário bruto: R$", salarioBruto)
print("Valor pago ao IR: R$", impostoRenda)
print("Valor pago ao inss: R$", inss)
print("Valor pago ao sindicato: R$", sindicato)
print("Foram descontados: R$", descontos)
print("Salário liquido: R$", salarioLiquido)