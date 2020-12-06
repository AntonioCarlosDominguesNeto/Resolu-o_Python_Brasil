#Exercicio 3: Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
nome = str(input("Digite seu nome: "))
tamanho = len(nome)
for n in range(1, tamanho + 1, 1):
    print(nome[n - 1])