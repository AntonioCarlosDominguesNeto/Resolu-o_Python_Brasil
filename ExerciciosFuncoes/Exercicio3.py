#Exercicio 3: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma():
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    n3 = int(input("Digite o terceiro numero: "))
    resultado = n1 + n2 + n3
    print(n1, "+", n2, "+", n3, "=", resultado)

soma()