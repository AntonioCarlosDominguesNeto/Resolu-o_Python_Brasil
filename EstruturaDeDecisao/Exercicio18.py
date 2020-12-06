#Desafio 18: Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida
data = str(input("Digite uma data: "))
a = int(data[5:])
m = int(data[2:4])
d = int(data[:1])

if d >= 1 and d <= 30:
    if m >= 1 and m <= 12:
        if a <= 1:
            print('Data invalida!')
        else:
            print('Data valida!')
    else:
        print('Data invalida!')
else:
    print('Data invalida!')
