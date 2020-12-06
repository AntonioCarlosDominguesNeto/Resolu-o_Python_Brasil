'''
Exercicio 21:
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 
reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade 
de notas existentes na máquina.
 A. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma 
 nota de 5 e uma nota de 1;
 B. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro
notas de 10, uma nota de 5 e quatro notas de 1.
'''
saque = int(input("Digite um numero de 10 a 600 que deseja sacar: "))
quantidade100 = 0
quantidade50 = 0
quantidade10 = 0
quantidade5 = 0
quantidade1 = 0

if saque >= 10 and saque <= 600:
    quantidade100 = saque / 100
    quantidade50 = (saque - (quantidade100 * 100)) / 50
    quantidade10 = (saque - (quantidade100 * 100) - (quantidade50 * 50)) / 10
    quantidade5 = (saque - (quantidade100 * 100) - (quantidade50 * 50) - (quantidade10 * 10)) / 5
    quantidade1 = saque - (quantidade100 * 100) - (quantidade50 * 50) - (quantidade10 * 10) - (quantidade5 * 5)    
else:
    print("Numero invalido!")

print(
    "Notas de 100:", quantidade100,
    "Notas de 50:", quantidade50,
    "Notas de 10:", quantidade10,
    "Notas de 5:", quantidade5,
    "Notas de 1:", quantidade1
)