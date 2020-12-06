'''
Exercicio 31: O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma 
loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá 
receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser 
informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e 
perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta 
operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme 
o exemplo abaixo:

Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
'''
contador = 0
soma = 0

dinheiro = float(input("Digite o quanto ele pagou: "))
quantidadeProdutos = int(input("Digite quantos produtos foram comprados: "))

for n in range(1, quantidadeProdutos + 1, 1):
    preco = float(input("Digite o preço do produto: "))
    soma += preco

if dinheiro < soma: 
    total = soma - dinheiro
    print("Total:", soma)
    print("O cliente ficou devendo:", total)
elif dinheiro > soma:
    total = dinheiro - soma
    print("Total:", soma)
    print("O troco é de:", total)
else:
        print("Total:", soma)
        print("Não precisa de troco")