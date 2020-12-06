#Exercicio 17: Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
numero = int(input("Digite um numero para fatorar: "))
denominador = numero - 1

while denominador != 1:
    numero = numero * denominador 
    denominador -= 1
print(numero)   