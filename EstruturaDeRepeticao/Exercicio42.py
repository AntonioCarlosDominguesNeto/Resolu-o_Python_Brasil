#Exercicio 42: Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0

while True:
    numero = int(input("Entre com um numero: "))
    if numero >= 0 and numero <= 25:
        contador1 += 1
    elif numero >= 26 and numero <= 50:
        contador2 += 1
    elif numero >= 51 and numero <= 75:
        contador3 += 1
    elif numero >= 76 and numero <= 100:
        contador4 += 1
    elif numero > 100:
        print("Numero invalido")
    else:
        break

print("Numeros entre 0 e 25:", contador1)
print("Numeros entre 26 e 50:", contador2)
print("Numeros entre 51 e 75:", contador3)
print("Numeros entre 76 e 100:", contador4)