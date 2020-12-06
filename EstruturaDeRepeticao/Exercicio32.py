#Exercicio 32: Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
numero = int(input("Que numero você deseja fatorar: "))
contador = numero - 1
fatorial = numero 

print(numero,"! =", end=" ")
print(numero - 1, ". ", end=" ")
while contador != 1:
    numero *= contador
    contador -= 1
    print(contador,". ", end=" ")
print("=", end=" ")
print(numero)