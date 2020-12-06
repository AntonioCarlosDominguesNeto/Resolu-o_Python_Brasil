#Exercicio 8: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
p1 = float(input("Digite o preço do primeiro produto: R$"))
p2 = float(input("Digite o preço do segundo produto: R$"))
p3 = float(input("Digite o preço do terceiro produto: R$"))
menor  = 9999999999999999999
produto = ""

if p1 < menor:
    menor = p1
    produto = "Primeiro produto"
if p2 < menor:
    menor = p2 
    produto = "Segundo produto"
if p3 < menor:
    menor = p3
    produto = "Terceiro produto"

print("Você deve comprar o", produto)