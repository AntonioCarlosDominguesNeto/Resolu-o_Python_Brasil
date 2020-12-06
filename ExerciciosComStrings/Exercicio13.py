'''
Exercicio 13: Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra 
que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e 
escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve 
ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
'''
import random

palavra1 = "Primeira Palavra"
palavra2 = "Segunda Palavra"
palavra3 = "Terceira Palavra"
palavra4 = "Quarta Palavra"
palavra5 = "Quinta Palavra"
palavra6 = "Sexta Palavra"
palavra7 = "Sétima Palavra"
palavra8 = "Oitava Palavra"
palavra9 = "Nona Palavra"
palavra10 = "Décima Palavra"
palavra11 = "Décima primeira Palavra"
palavra12 = "Décima segunda Palavra"
palavra13 = "Décima terceira Palavra"
palavra14 = "Décima quarta Palavra"
palavra15 = "Décima quinta Palavra"
palavra16 = "Décima sexta Palavra"
palavra17 = "Décima sétima Palavra"
palavra18 = "Décima oitava Palavra"
palavra19 = "Décima nona Palavra"
palavra20 = "Vigésima Palavra"
sorteada = random.randint(1, 20)

if sorteada == 1:
    resultadoPalavra = palavra1
    resultado = 1
elif sorteada == 2:
    resultadoPalavra = palavra2
    resultado = 2
elif sorteada == 3:
    resultadoPalavra = palavra3
    resultado = 3
elif sorteada == 4:
    resultadoPalavra = palavra4
    resultado = 4
elif sorteada == 5:
    resultadoPalavra = palavra5
    resultado = 5
elif sorteada == 6:
    resultadoPalavra = palavra6
    resultado = 6
elif sorteada == 7:
    resultadoPalavra = palavra7
    resultado = 7
elif sorteada == 8:
    resultadoPalavra = palavra8
    resultado = 8
elif sorteada == 9:
    resultadoPalavra = palavra9
    resultado = 9
elif sorteada == 10:
    resultadoPalavra = palavra10
    resultado = 10
elif sorteada == 11:
    resultadoPalavra = palavra11
    resultado = 11
elif sorteada == 12:
    resultadoPalavra = palavra12
    resultado = 12
elif sorteada == 13:
    resultadoPalavra = palavra13
    resultado = 13
elif sorteada == 14:
    resultadoPalavra = palavra14
    resultado = 14
elif sorteada == 15:
    resultadoPalavra = palavra15
    resultado = 15
elif sorteada == 16:
    resultadoPalavra = palavra16
    resultado = 16
elif sorteada == 17:
    resultadoPalavra = palavra17
    resultado = 17
elif sorteada == 18:
    resultadoPalavra = palavra18
    resultado = 18
elif sorteada == 19:
    resultadoPalavra = palavra19
    resultado = 19
else:
    resultadoPalavra = palavra20
    resultado = 20

for n in range(1, 7, 1):
    chute = int(input("Digite o numero da palavra que você acha que foi sorteada: "))
    if chute == resultado:
        print("Você ganhou!")
        break        
    else:
        print("Você errou!")

print("Palavra sorteada:", resultadoPalavra)