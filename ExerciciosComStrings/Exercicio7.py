'''
Exercicio 7: Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

A. quantos espaços em branco existem na frase.
B. quantas vezes aparecem as vogais a, e, i, o, u.
'''
contadorEspaco = 0
contadorVogais = 0
frase = str(input("Digite uma frase: ")).upper()

for n in frase:
    if n == " ":
        contadorEspaco += 1

    if n in "AEIOU":
        contadorVogais += 1

print("Quantidade de espaços:", contadorEspaco)
print("Quantidade de vogais:", contadorVogais)