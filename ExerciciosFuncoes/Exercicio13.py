'''
Exercicio 13: Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| 
‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo 
igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para 
valores dentro da faixa de forma elegante.
'''
def retangulo():
    linhas = []
    colunas = []
    linha = int(input("Digite a quantidade de linhas de 0 a 20: "))
    coluna = int(input("Digite o numero de colunas de 0 a 20: "))
    linhas.append(linha)
    colunas.append(coluna)

    if linha > 20 or linha < 0 or coluna > 20 or coluna < 0:
        print("Numero inválido!")
    else:
        linha = '+'
        for l in range(len(linhas)):
            linha += '-'
        linha += '+'
        print (linha)

        for c in range(len(colunas)):
            coluna = '|'
            coluna += ' ' * len(linhas)
            coluna += '|'
            print(coluna)

retangulo()