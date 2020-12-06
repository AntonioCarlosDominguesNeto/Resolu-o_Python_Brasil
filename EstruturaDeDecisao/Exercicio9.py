#Exercicio 9: Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))
n3 = float(input("Digite um numero: "))
primeiro = 0
segundo = 0
terceiro = 0

if (n1 > n2) and (n1 > n3):
    if n2 > n3:
        terceiro = n3
        segundo = n2
    else:
        terceiro = n2
        segundo = n3
    primeiro = n1
elif (n2 > n3) and (n2 > n1): 
    if n3 > n1:
        terceiro = n1
        segundo = n3
    else:
        terceiro = n3
        segundo = n1
    primeiro = n2
else:
    if n2 > n1:
        terceiro = n1
        segundo = n2
    else:
        terceiro = n2
        segundo = n1
    primeiro = n3

print("Numeros em ordem decrecente:", primeiro, segundo, terceiro)