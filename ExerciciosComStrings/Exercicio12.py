#Exercicio 12:Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
numeros = []
numero = str(input("Digite o numero de telefone: "))
tamanho = len(numero)
for n in range(0, tamanho, 1):
    numeros.append(numero[n])
tamanhos = len(numeros)
if tamanhos - 1 > 9:
    print("Numero inválido")
else:
    if tamanhos - 1 == 7 and numeros[4] in "-":
        print("Irei adicionar o 3, pois você não digitiou o numero completo")
        numeros.insert(-1, "3")
        print(numeros)
    elif tamanho - 1 == 6:
        print("Irei adicionar o 3, pois você não digitiou o numero completo")
        numeros.insert(-1, "3")
        print(numeros)
    else:
        print(numero) 