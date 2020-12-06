#Exercicio 49: Faça um programa que mostre os n termos da Série a seguir: S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
n1 = int(input("Informe a quantidade de termos: "))
denominador = 1
soma = 0
contador = 0

for n in range(1, n1 + 1, 1):
    soma += contador / denominador
    denominador += 2
    contador += 1

print("Sequencia:", soma)