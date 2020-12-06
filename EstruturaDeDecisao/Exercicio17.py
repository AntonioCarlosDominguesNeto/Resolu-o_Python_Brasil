#Exercicio 17: Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
anoBissexto = int(input("Digite o ano: "))

if(anoBissexto % 4 == 0 and anoBissexto % 100 != 0 or anoBissexto % 400 == 0):
    print("É bissexto!")
else:
    print("Não é bissexto!")