#Exercicio 35: Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
numero = int(input("Digite até que numero: "))
contador = 1
contadorDivisao = 0

while contador < numero:
    if numero % contador == 0:
        contadorDivisao += 1
        divisivel = contador
        print("Numeros que são divisiveis:", divisivel)
    contador += 1

if contadorDivisao == 2:
    print("O numero", numero, "é primo!")
else:
    print("O numero", numero, "não é primo!")