#Exercicio 13: Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resposta = 1

for r in range(1, expoente + 1, 1):
    resposta = resposta * base    
print(base, "elevado a", expoente, "é:",  resposta)