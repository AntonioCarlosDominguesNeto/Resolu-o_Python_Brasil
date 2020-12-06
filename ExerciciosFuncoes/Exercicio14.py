#Exercicio 14: Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
def quadrado():
    quadradoMagico1 = []
    quadradoMagico2 = []
    quadradoMagico3 = []
    contador = 0
    while contador != 9:
        numero = int(input("Digite um numero de 0 a 9: "))
        if numero < 0 or numero > 9:
            print("Numero invalido!")
            contador -= 1
        else:
            if contador == 1 or contador == 2 or contador == 3:
                quadradoMagico1.append(numero)
            elif contador == 4 or contador == 5 or contador == 6:
                quadradoMagico2.append(numero)
            else:
                quadradoMagico3.append(numero)
        contador += 1

    print(quadradoMagico1)
    print(quadradoMagico2)
    print(quadradoMagico3)

quadrado()