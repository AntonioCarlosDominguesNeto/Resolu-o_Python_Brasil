#Exercicio 26: Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
numeroEleitores = int(input("Digite quantos eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
votosInvalidos = 0

if numeroEleitores > 0:
    for n in range(1, numeroEleitores + 1, 1):
        voto = int(input("Digite em qual candidato você irá votar[1/2/3]: "))
        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        else:
            votosInvalidos += 1
else:
    print("Numero de eleitores invalido!")

print("Quantidade de votos do primeiro candidato:", candidato1)
print("Quantidade de votos do segundo candidato:", candidato2)
print("Quantidade de votos do terceiro candidato:", candidato3)
print("Quantidade de votos invalidos:", votosInvalidos)