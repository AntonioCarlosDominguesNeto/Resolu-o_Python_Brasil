#Exercicio 41: Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
divida = float(input("Digite o valor da divida: "))
contadorJuros = 0
valorJuros = 0

for n in range(1, 13, 1):
    print("Valor do juros:", valorJuros)
    contadorJuros += 1
    
    if contadorJuros >= 0 and contadorJuros < 3:
        valorJuros = 0
        descontoJuros = divida * valorJuros
        valorFinal = divida + descontoJuros
    elif contadorJuros >= 3 and contadorJuros < 6:
        valorJuros = 0.10
        descontoJuros = divida * valorJuros
        valorFinal = divida + descontoJuros
    elif contadorJuros >= 6 and contadorJuros < 9:
        valorJuros = 0.15
        descontoJuros = divida * valorJuros
        valorFinal = divida + descontoJuros
    elif contadorJuros >= 9 and contadorJuros < 12:
        valorJuros = 0.20
        descontoJuros = divida * valorJuros
        valorFinal = divida + descontoJuros
    else:
        valorJuros = 0.25
        descontoJuros = divida * valorJuros
        valorFinal = divida + descontoJuros
    
    print("Parcela:", contadorJuros, "Juros:", valorJuros, "Divida final:", valorFinal)