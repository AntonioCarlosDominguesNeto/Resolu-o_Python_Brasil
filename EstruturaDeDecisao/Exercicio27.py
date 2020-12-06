'''
Exercicio 27: Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um 
desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade 
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
fruta = int(input("Digite se você comprou morango ou maçã[1/2]: "))

if fruta == 1:
    kgs = float(input("Digite quantos kgs você consumiu: "))
    if kgs <= 5 and kgs >= 0:
        precoKgs = 2.50
        preco = precoKgs * kgs
        if preco > 25:
            desconto = preco * 0.10
            precoDesconto = preco - desconto
    elif kgs > 5 and kgs <=8:
        precoKgs = 2.20
        preco = precoKgs * kgs
        if preco > 25:
            desconto = preco * 0.10
            precoDesconto = preco - desconto
    elif kgs > 8:
        precoKgs = 2.20
        preco = precoKgs * kgs
        desconto = preco * 0.10
        precoDesconto = preco - desconto
    else:
        print("Numero invalido!")
elif fruta == 2:
    kgs = float(input("Digite quantos kgs você consumiu: "))
    if kgs <= 5 and kgs >= 0:
        precoKgs = 1.80
        preco = precoKgs * kgs
        if preco > 25:
            desconto = preco * 0.10
            precoDesconto = preco - desconto
    elif kgs > 5 and kgs <=8:
        precoKgs = 1.50
        preco = precoKgs * kgs
        if preco > 25:
            desconto = preco * 0.10
            precoDesconto = preco - desconto
    elif kgs > 8:
        precoKgs = 1.50
        preco = precoKgs * kgs
        desconto = preco * 0.10
        precoDesconto = preco - desconto
    else:
        print("Numero invalido!")
else:
        print("Numero invalido!")

print("Conta: R$", precoDesconto)