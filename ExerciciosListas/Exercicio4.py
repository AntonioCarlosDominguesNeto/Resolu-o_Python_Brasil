#Exercicio 4: Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
caracteres = []
vogais = "AEIOU"
consoantes = []
contador = 0

for n in range(1, 11, 1):
    caracteres.append(input("Digite uma caractere: ").upper().split()[0])
    if caracteres[n - 1] not in vogais:
        consoantes.append(caracteres[n - 1])
        contador += 1

print("Caracteres digitados:", caracteres)
print("Consoantes digitadas:", consoantes)
print("Quantidade de consoantes:", contador)