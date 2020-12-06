'''
Exercicio 11: Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva 
uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja 
inválida.
'''
def mesPorExtenso():
    mes = int(input("Digite o numero do mês: "))
    if mes == 1:
        mesExtenso = "Janeiro"
        print(mesExtenso)
    elif mes == 2:
        mesExtenso = "Fevereiro"
        print(mesExtenso)
    elif mes == 3:
        mesExtenso = "Março"
        print(mesExtenso)
    elif mes == 4:
        mesExtenso = "Abril"
        print(mesExtenso)
    elif mes == 5:
        mesExtenso = "Maio"
        print(mesExtenso)
    elif mes == 6:
        mesExtenso = "Junho"
        print(mesExtenso)
    elif mes == 7:
        mesExtenso = "Julho"
        print(mesExtenso)
    elif mes == 8:
        mesExtenso = "Agosto"
        print(mesExtenso)
    elif mes == 9:
        mesExtenso = "Setembro"
        print(mesExtenso)
    elif mes == 10:
        mesExtenso = "Outubro"
        print(mesExtenso)
    elif mes == 11:
        mesExtenso = "Novembro"
        print(mesExtenso)
    elif mes == 12:
        mesExtenso = "Dezembro"
        print(mesExtenso)
    else:
        print("Mês inválido!")

mesPorExtenso()