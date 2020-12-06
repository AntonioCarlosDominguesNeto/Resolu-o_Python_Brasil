#Exercicio 19: Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
quantidade = int(input("Digite quantos numeros voce irá adicionar: "))
maior = 0
menor = 999999999999999999999999999999999999999999999999
soma = 0

if quantidade > 0 and quantidade <= 1000:
    for n in range(1, quantidade + 1, 1):
        numero = int(input("Digite um numero: "))
        soma += numero    
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    print("Maior numero:", maior)
    print("Menor numero:", menor)
    print("Soma entre todos:", soma)
else:
    print("Valor invalido!")