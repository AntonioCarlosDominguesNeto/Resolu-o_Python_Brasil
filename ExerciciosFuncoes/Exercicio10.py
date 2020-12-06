'''
Exercicio 10: Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, 
obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você 
tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez 
um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número 
novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''
import random

def craps():
    dado = random.randint(2, 12)
    if dado == 7 or dado == 11:
        print("Você é um natural!")
        print("Você ganhou!")
    elif dado == 2 or dado == 3 or dado == 12:
        print("Você é craps!")
        print("Você perdeu!")
    else:
        while True:
            dadoFinal = dado
            dado = random.randint(2, 12)
            if dado == 7:
                print("Você perdeu!")
                break
            elif dado == dadoFinal:
                print("Você ganhou!")
                break

craps()