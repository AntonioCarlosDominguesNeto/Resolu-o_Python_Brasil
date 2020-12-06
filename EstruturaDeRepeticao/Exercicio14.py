#Exercicio 14: Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares
par = 0
impar = 0

for i in range(1, 11, 1):
    numero = int(input("Digite um numero inteiro: "))
    if numero / 2 % 1:
        impar += 1
    else:
        par += 1

print("Quantidade de numeros pares:", par)
print("Quantidade de numeros impares:", impar)