#Exercicio 1: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = int(input("Digite uma nnota de 0 a 10: "))
    if nota >= 0 and nota <=10:
        print("A nota digitada foi:", nota)
        break
    else:
        print("Nota invalida!")
