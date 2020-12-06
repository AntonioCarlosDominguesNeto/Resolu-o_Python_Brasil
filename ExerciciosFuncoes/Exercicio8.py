#Exercicio 8: Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def contador():
    numero = int(input("Digite um numero inteiro: "))
    numeroQuantidade = len(str(numero))
    print("Quantidade de digitos do numero:", numeroQuantidade)

contador()