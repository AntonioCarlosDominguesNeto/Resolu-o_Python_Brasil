#Exercicio 20: Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
while True:
    numero = int(input("Digite um numero para fatorar: "))
    if numero > 16 or numero <=0:
        print("Não é possivel fatorar esse numero!")
    else:
        denominador = numero - 1
        while denominador != 1:
            numero = numero * denominador 
            denominador -= 1
        print(numero)   
        continuar = str(input("Digite se você deseja continuar[S/N]: ")).upper().split()[0]
        if continuar in "N":
            break