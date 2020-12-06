'''
Exercicio 5: Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item 
antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''
def somaImposto():
    preco = float(input("Digite o preço do produto sem imposto: "))
    taxaImposto = preco * 0.10
    precoFinal = preco + taxaImposto
    print("Preço inicial:", preco)
    print("Pocentagem do imposto: 10%")
    print("Adição de imposto:", taxaImposto)
    print("Preço final:", precoFinal)

somaImposto()