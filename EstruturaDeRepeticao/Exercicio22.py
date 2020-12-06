#Exercicio 22: Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
numero = int(input("Digite um numero: "))
contadorDivisao = 0

for n in range(1, 11, 1):
    if numero % n == 0:
        contadorDivisao += 1
        divisivel = n
        print("Numeros que são divisiveis:", divisivel)

if contadorDivisao == 2:
    print("O numero", numero, "é primo!")
else:
    print("O numero", numero, "não é primo!")