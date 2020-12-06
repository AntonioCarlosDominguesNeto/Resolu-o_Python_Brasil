#Exercicio 3: Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
for n in range(1, 5, 1):
    notas.append(int(input("Digite a nota: ")))
print("A média foi:", sum(notas) / 4)