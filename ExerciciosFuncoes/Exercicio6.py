'''
Exercicio 6: Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o 
programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas 
funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.
M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. 
ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as 
vezes que desejar.
'''
def conversao():
    while True:
        numeros = 0
        numero = int(input("Digite que horão são: "))
        if numero >= 0 and numero <= 12:
            print("São:", numero, "A.M.")
        elif numero == 13:
            numeros = 1
            print("São", numeros, "P.M.")
        elif numero == 14:
            numeros = 2
            print("São", numeros, "P.M.")
        elif numero == 15:
            numeros = 3
            print("São", numeros, "P.M.")
        elif numero == 16:
            numeros = 4
            print("São", numeros, "P.M.")
        elif numero == 17:
            numeros = 5
            print("São", numeros, "P.M.")
        elif numero == 18:
            numeros = 6
            print("São", numeros, "P.M.")
        elif numero == 19:
            numeros = 7
            print("São", numeros, "P.M.")
        elif numero == 20:
            numeros = 8
            print("São", numeros, "P.M.")
        elif numero == 21:
            numeros = 9
            print("São", numeros, "P.M.")
        elif numero == 22:
            numeros = 10
            print("São", numeros, "P.M.")
        elif numero == 23:
            numeros = 11
            print("São", numeros, "P.M.")
        else:
            print("Numero inválido!")
        continuar = str(input("Disige se deseja continuar ou não[S/N]: ")).upper().split()[0]
        if continuar in "N":
            break

conversao()