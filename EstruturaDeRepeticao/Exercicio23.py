'''
Exercicio 23: Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo
usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números 
primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''
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