'''
Exercicio 2: Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
'''
numero = int(input('Digite o número: '))

def numeros(numero):
    for c in range(1, numero + 1, 1):
        saida = []
        for c2 in range(c):
            saida.append(str(c2 + 1))
        print("".join(saida))

numeros(numero)