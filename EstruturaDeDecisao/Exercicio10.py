#Exercicio 10: Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
periodo = str(input("Digite o periodo em que você estuda[M/V/N]: ")).upper().split()[0]

if periodo in "M":
    print("Bom dia!")
elif periodo in "V":
    print("Boa tarde!")
elif periodo in "N":
    print("Boa noite!")
else:
    print("Valor inválido!")  