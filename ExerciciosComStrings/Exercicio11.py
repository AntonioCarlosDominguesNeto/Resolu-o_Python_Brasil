#Exercicio 11: Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
forcaFinal = []
tamanhoForca = len(forcaFinal)
forca = str(input("Digite a forca: ")).upper().strip()
forcaFinal.append(forca)
quantidadeErros = 0
chutes = []
while True:
    print("Quantidade de erros:", quantidadeErros)
    chute = str(input("Digite uma letra: ")).upper().strip()
    for n in range(1, tamanhoForca + 1, 1):
        if chute == forcaFinal[n - 1]:
            print(forcaFinal[n - 1])
        else:
            quantidadeErros += 1

    if chutes in forcaFinal:
        print("Você ganhou!")
        break
    elif quantidadeErros > 6:
        print("Você perdeu!")
        break    