#Exercicio 2: Analisador de logs do Apache. Desenvolva um analisador de log do Apache que mostre quais as strings de pesquisa do google que mais levam internautas para o site da sua organização.
pesquisa1 = "Pesquisa1"
pesquisa2 = "Pesquisa2"
pesquisa3 = "Pesquisa3"
pesquisa4 = "Pesquisa4"
pesquisa5 = "Pesquisa5"
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
while True:
    resultado = int(input("Digite qual das pequisas de levou ao site[1/2/3/4/5]: "))
    if resultado == 1:
        contador1 += 1

    if resultado == 2:
        contador2 += 1

    if resultado == 3:
        contador3 += 1

    if resultado == 4:
        contador4 += 1

    if resultado == 5:
        contador5 += 1

    continuar = str(input("Deseja continuar[S/N]: ")).upper().split()[0]
    if continuar in "N":
        break

print("Quantidade do 1°", contador1)
print("Quantidade do 2°", contador2)
print("Quantidade do 3°", contador3)
print("Quantidade do 4°", contador4)
print("Quantidade do 5°", contador5)