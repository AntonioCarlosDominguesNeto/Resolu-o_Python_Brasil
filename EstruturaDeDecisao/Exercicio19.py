'''
Exercicio 19: Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1,
7 e 16
'''
n = int(input("Digite um numero menor que 1000: "))
c = n / 100
d = (n - (c * 100)) / 10
u = (n - (c * 100) - (d * 10))
x = ""

if n >= 1000:
    print("Numero invalido!")
else: 
    if c > 0:
        x = x + str(c)
        if c > 1:
            x = x + "Centenas"
        else:
            x = x + "Centena"
    elif u > 0:
        if c != 0 or d != 0:
            x = x + "e"
        x = x + str(u)
        if u > 1:
            x = x + "Unidades"
        else:
            x = x + "Unidade"
    elif d > 0:
        if u == 0 and c != 0:
            x = x + "e"
        x = x + str(d)
        if d > 1:
            x = x + "Dezenas"
        else:
            x = x + "Dezena"
    else:
        print("Numero desconhecido!")