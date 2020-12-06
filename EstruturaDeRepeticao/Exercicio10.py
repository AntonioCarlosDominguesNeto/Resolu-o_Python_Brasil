#Exercicio 10: Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))

if n1 < n2:
    for n in range(n1 + 1, n2, 1):
        print(n, end=" ")
elif n1 > n2:
    for n in range(n2 + 1, n1, 1):
        print(n, end=" ")
else:
    print("Não há numeros entre eles!")