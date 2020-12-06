#Exercicio 5: Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
par = []
impar = []
numero = []
for n in range(1, 21, 1):
    numero.append(int(input("Digite um numero: ")))
    if numero[n - 1] % 2 == 1:
        impar.append(numero[n - 1])
    else:
        par.append(numero[n - 1])
    
print("Numeros digitados: ", numero)
print("Numeros pares: ", par)
print("Numeros impares", impar)