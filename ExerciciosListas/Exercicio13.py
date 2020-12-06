#Exercicio 13: Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
mesFinal = []
resultado = []
mesExtenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for n in range(1, 13, 1):
    mes = float(input("Digite a temperatura: "))
    mesFinal.append(mes)
    
media = sum(mesFinal) / 12

contador  = 0
for mes in mesExtenso:
    if mesFinal[contador] > media:
        print(mesExtenso[contador])
    contador += 1
