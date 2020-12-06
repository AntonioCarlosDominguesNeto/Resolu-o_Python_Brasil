#Exercicio 28: Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
quantidadeCds = int(input("Digite quantos cds, você já comprou: "))
soma = 0

if quantidadeCds > 0:
    for n in range(1, quantidadeCds + 1, 1):
        preco = float(input("Digite o preço em que você pagou: "))
        soma += preco
    media = soma / quantidadeCds    
    print("Quantidade de gastos:", soma)
    print("Média de gastos:", media)
elif quantidadeCds == 0:
    print("Então você não gastou nada!")
else:
    print("Numero invalido")