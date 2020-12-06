#Exercicio 11: Altere o programa anterior para mostrar no final a soma dos números.
n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))
soma = 0 

if n1 < n2:
    for n in range(n1 + 1, n2, 1):
        soma += n
elif n1 > n2:
    for n in range(n2 + 1, n1, 1):
        soma += n
else:
    print("Não há numeros entre eles!")

print("A soma foi:", soma)