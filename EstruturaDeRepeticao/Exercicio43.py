'''
Exercicio 43: O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser 
pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o 
pedido deve ser encerrado.
'''
soma = 0
soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
soma6 = 0
preco1 = 1.20
preco2 = 1.30
preco3 = 1.50
preco4 = 1.20
preco5 = 1.30
preco6 = 1.00

while True:
    codigo = int(input("Digite o código do seu pedido[100/101/102/103/104/105/0]: "))
    if codigo == 100:
        quantidade = int(input("Digite a quantidade: "))
        soma1 = preco1 * quantidade
    elif codigo == 101:
        quantidade = int(input("Digite a quantidade: "))
        soma2 = preco2 * quantidade
    elif codigo == 102:
        quantidade = int(input("Digite a quantidade: "))
        soma3 = preco3 * quantidade
    elif codigo == 103:
        quantidade = int(input("Digite a quantidade: "))
        soma4 = preco4 * quantidade
    elif codigo == 104:
        quantidade = int(input("Digite a quantidade: "))
        soma5 = preco5 * quantidade
    elif codigo == 105:
        quantidade = int(input("Digite a quantidade: "))
        soma6 = preco6 * quantidade
    elif codigo == 0:
        break
    else:
        print("Código invalido!")

soma = soma1 + soma2 + soma3 + soma4 + soma5 + soma6
print("Total a ser pago:", soma)