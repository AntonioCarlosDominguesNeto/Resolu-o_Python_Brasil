'''
Exercicio 11: As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
 o salários até R$ 280,00 (incluindo) : aumento de 20%
 o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
 o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
 o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
 o salário antes do reajuste;
 o percentual de aumento aplicado;
 o valor do aumento;
 o novo salário, após o aumento.
'''
salario = float(input("Digite o valor do seu salário: "))

if salario <= 280.00:
    percentual = 20
    ajuste = 0.20
    valorAjuste = salario * ajuste
    salarioAjustado = salario + valorAjuste  
elif salario <= 700.00:
    percentual = 15
    ajuste = 0.15
    valorAjuste = salario * ajuste
    salarioAjustado = salario + valorAjuste    
elif salario < 1500.00:
    percentual = 10
    ajuste = 0.10
    valorAjuste = salario * ajuste
    salarioAjustado = salario + valorAjuste
elif salario >= 1500.00:
    percentual = 5
    ajuste = 0.05
    valorAjuste = salario * ajuste
    salarioAjustado = salario + valorAjuste
else:
    print("Valor inválido!")

print("Salário antes do reajuste: R$", salario)
print("Percentual de aumento aplicado:", percentual,"%")
print("Valor do aumento: R$", valorAjuste)
print("Salário reajustado: R$", salarioAjustado)