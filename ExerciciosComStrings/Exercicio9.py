'''
Exercicio 9 : Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato 
xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos 
caracteres de formatação.
'''
cpf = int(input("Digite seu cpf: "))

if len(cpf) > 13:
    print("Cpf inválido")
else:
    print("Cpf valido")   