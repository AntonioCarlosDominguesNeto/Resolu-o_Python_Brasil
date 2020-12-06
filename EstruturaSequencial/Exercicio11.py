'''
Exercicio 11: Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    A. o produto do dobro do primeiro com metade do segundo.
    B. a soma do triplo do primeiro com o terceiro.
    C. o terceiro elevado ao cubo.
'''
numeroInteiro1 = int(input("Digite o primeiro numero inteiro: "))
numeroInteiro2 = int(input("Digite o segundo numero inteiro: "))
numeroReal = float(input("Digite um numero real: "))
a = (numeroInteiro1 * 2) * (numeroInteiro2 * 0.5)
b = (numeroInteiro1 * 3) + numeroReal
c = numeroReal ** 3

print("O produto do dobro do primeiro com metade do segundo é:", a)
print("A soma do triplo do primeiro com o terceiro é:", b)
print("O terceiro elevado ao cubo é:", c)