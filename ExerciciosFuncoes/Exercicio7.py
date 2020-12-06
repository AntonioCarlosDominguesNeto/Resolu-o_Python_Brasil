'''
Exercicio 7: Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma 
prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso 
e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao 
programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa 
deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero 
para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a 
quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. 
Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de 
juros por dia de atraso.
'''
def valorPagamento():
    valores = []
    while True:
        valorInicial = float(input("Digite o valor da prestação: "))
        atraso = int(input("Digite quantos dias de atraso: "))
        porcentagemAtraso = 0
        
        for n in range(0, atraso, 1):
            porcentagemAtraso += 0.01
        
        if atraso == 0:
            print("O valor é de:", valorInicial)
            valores.append(valorInicial)
        elif atraso > 0 :
            taxa = (valorInicial * 0.3) * porcentagemAtraso
            valorFinal = valorInicial + taxa
            print("O valor é de:", valorFinal)
            valores.append(valorFinal) 
        else:
            print("Valor invalido!")
        
        continuar = int(input("Se deseja parar de digitar valores digite 0: "))

        if continuar == 0:
            break
    
    print("Valores do dia:", valores)

valorPagamento()