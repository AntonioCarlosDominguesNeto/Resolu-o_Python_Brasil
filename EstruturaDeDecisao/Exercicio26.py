'''
Exercicio 26: Um posto está vendendo combustíveis com a seguinte tabela de descontos:
A. Álcool:
B. até 20 litros, desconto de 3% por litro
C. acima de 20 litros, desconto de 5% por litro
D. Gasolina:
E. até 20 litros, desconto de 4% por litro
F. acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o
tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
combustivel = str(input("Digite se você utilizou Alcool ou Gasolina[A/G]: ")).upper().split()[0]

if combustivel in "A":
    precoAlcool = 1.90
    litros = int(input("Digite quantos litros de Alcool você consumiu: "))
    if litros <= 20:
        preco = precoAlcool * litros
        desconto = preco * 0.03
        precoFinal = preco - desconto
        print("Preço final:", precoFinal)
    elif litros > 20:
        preco = precoAlcool * litros
        desconto = preco * 0.05
        precoFinal = preco - desconto
        print("Preço final:", precoFinal)
    else:
        print("Numero invalido!")
elif combustivel in "G":
    precoGasolina = 2.50
    litros = int(input("Digite quantos litros de Gasolina você consumiu: "))
    if litros <= 20:
        preco = precoGasolina * litros
        desconto = preco * 0.04
        precoFinal = preco - desconto
        print("Preço final:", precoFinal)
    elif litros > 20:
        preco = precoGasolina * litros
        desconto = preco * 0.06
        precoFinal = preco - desconto
        print("Preço final:", precoFinal)
    else:
        print("Numero invalido!")
else:
    print("Opção invalida!")