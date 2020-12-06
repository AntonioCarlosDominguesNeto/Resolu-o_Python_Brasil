'''
Exericio 1: Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''
def numeros(numero):
    return list(str(numero) * numero)

numero = int(input("Digite um numero: "))

for c in range(0, 5, 1):
    print(numeros(c))