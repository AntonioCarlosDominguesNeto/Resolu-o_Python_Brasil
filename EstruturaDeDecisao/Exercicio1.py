#Exercicio 1: Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print("O", n1, "que é o primeiro numero, é maior que o", n2)
elif n2 > n1:
    print("O", n2, "que é o segundo numero, é maior que o", n1)
else:
    print("Os dois têm o mesmo valor")