#Exercicio 4: Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
nome = str(input("Digite seu nome: "))
tamanho = len(nome)
contador = 0
for n in range(1, tamanho + 2, 1):
    print(nome[contador : n - 1])
