#Exercicio 9: Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverso():
    numero = str(input("Digite um numero: "))

    print("Numero ao contrario:", str(numero[::-1]))

reverso()