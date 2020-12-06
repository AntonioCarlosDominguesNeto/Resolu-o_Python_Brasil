'''
Exercicio 24:
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O
resultado da operação deve ser acompanhado de uma frase que diga se o número é:
A. par ou ímpar;
B. positivo ou negativo;
C. inteiro ou decimal.
'''
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
operacao = int(input("Podemos somar, subtrair, multiplicar ou dividir[1/2/3/4]: "))

if operacao == 1:
    resultado = n1 + n2
elif operacao == 2:
    resultado = n1 - n2
elif operacao == 3:
    resultado = n1 * n2
elif operacao == 4:
    resultado = n1 / n2
else:
    resultado = "Opção inválida!"

if resultado / 2 % 1:
    print("O numero", resultado, "é: Impar")
else:
    print("O numero", resultado, "é: Par")

if resultado >= 0 :
    print("O numero", resultado, "é: Positivo")
else:
    print("O numero", resultado, "é: Negativo")

if resultado == int(resultado):
    print("O numero", resultado, "é um numero: Real")
else:
    print("O numero", resultado, "é um numero: Decimal")