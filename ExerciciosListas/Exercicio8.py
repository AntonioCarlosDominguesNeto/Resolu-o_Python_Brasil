#Exercicio 8: Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idadeFinal = []
alturaFinal = []
contador = 0

while contador != 5:
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    idadeFinal.append(idade)
    alturaFinal.append(altura)
    print("\n")
    contador += 1

print("Idade em ordem inversa:", idadeFinal[::-1])
print("Altura em ordem inversa:", alturaFinal[::-1])