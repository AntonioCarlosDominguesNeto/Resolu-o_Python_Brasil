#Exercicio 50: Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
n1 = int(input("Informe a quantidade de termos: "))
denominador = 1
soma = 0
contador = 0
h = 1

for n in range(1, n1 + 1, 1):
    soma += contador / denominador
    h += h / n
    denominador += 2
    contador += 1

print("N:", soma)
print("H:", h)