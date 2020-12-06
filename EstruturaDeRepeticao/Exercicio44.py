'''
Exercicio 44: Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de 
código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
    ° O total de votos para cada candidato;
    ° O total de votos nulos;
    ° O total de votos em branco;
    ° A percentagem de votos nulos sobre o total de votos;
    ° A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o 
    valor zero.
'''
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
brancos = 0
nulos = 0
numeroEleitores = int(input("Digite a quantidade de eleitores: "))

for n in range(1, numeroEleitores + 1, 1):
    candidato = int(input("Digite em que candidato deseja votar[1/2/3/4]: "))
    if candidato == 1:
        candidato1 += 1
    elif candidato == 2:
        candidato2 += 1
    elif candidato == 3:
        candidato3 += 1
    elif candidato == 4:
        candidato4 += 1
    elif candidato == 0:
        nulos += 1
    else:
        brancos += 1
    
todosVotos = candidato1 + candidato2 + candidato3 + candidato4 + brancos + nulos
porcentagem1 = nulos / numeroEleitores
porcentagem2 = brancos / numeroEleitores

print("Votos em José:", candidato1)
print("Votos em João:", candidato2)
print("Votos em Maria:", candidato3)
print("Votos em Ana:", candidato4)
print("Votos nulos:", nulos)
print("Votos em Brancos:", brancos, "\n")
print("Porcentagem votos nulos:", porcentagem1,"%")
print("Porcentagem votos brancos:", porcentagem2,"%")