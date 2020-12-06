#Exercicio 6: Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",]
while True:
    dia = int(input("Digite o dia em que você nasceu: "))
    if dia < 0 or dia > 31:
        print("Dia inválido!")
    else:
        diaFinal = dia
        mes = int(input("Digite o mês em que você nasceu: "))
        if mes < 1 or mes > 12:
            print("Mês inválido!")
        else:
            mesFinal = mes        
            ano = int(input("Digite o ano em que você nasceu: "))
            print("Você nasceu no dia", diaFinal, "de", meses[mesFinal - 1], "de", ano)
            break