#Exercicio 36: Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário
numero = int(input("Digite que tabuada deseja saber: "))
comeco = int(input("Digite com que numero ela ira começar: "))
fim = int(input("Digite com que numero ela irá acabar: "))

if comeco <= fim:
    for n in range(comeco, fim + 1, 1):
        resultado = numero * comeco
        print(numero,"X", comeco, "=", resultado)
        comeco += 1
else:
    print("tabuada invalida!")