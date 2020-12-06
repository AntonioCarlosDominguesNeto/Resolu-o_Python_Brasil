#Exercicio 5: Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
nome = str(input("Digite seu nome: "))
tamanho = len(nome)

for n in range(tamanho, 0, -1):
   for n2 in range(0, n, 1):
       print(nome[n2], end=" ")
    
