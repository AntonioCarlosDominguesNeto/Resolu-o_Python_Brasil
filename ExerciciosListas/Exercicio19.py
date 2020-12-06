#Exercicio 19: Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações
votos = [0] * 6
votosExtenso = ["Unix", "Linux", "Windows", "Outros", "Netware", "MAC OS"]
voto = -1
contador = 0
contador2 = 1
vencedor = 0

while True:
    voto = int(input('Numero do jogador[1 até 6]: '))
    if voto == 0 or voto > 6:
        print("Valor inválido!")
    elif voto < 0:
        break
    else:
        votos[0] += 1
        if votos[contador] > vencedor:
            vencedor = votos[contador]
        contador += 1

print("Total de votos:", contador)
print("Vencedor:", votosExtenso[vencedor - 4])