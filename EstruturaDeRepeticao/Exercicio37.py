'''
Exercicio 37: Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da 
academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário 
digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do 
clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos 
clientes
'''
maior = 0
menor = 9999999999999999999999999999999999999999999999999999999
magro = 9999999999999999999999999999999999999999999999999999999
gordo = 0
codigoMaior = 0
codigoMenor = 0
codigoGordo = 0
codigoMagro = 0
somaAltura = 0
somaPeso = 0
contador = 0

while True:
    codigo = int(input("Digite seu código: "))
    altura = float(input("Digite sua altura: "))
    somaAltura += altura
    if altura > maior:
        maior = altura
        codigoMaior = codigo
    if altura < menor:
        menor = altura
        codigoMenor = codigo
    
    peso = float(input("Digite seu peso: "))
    somaPeso += peso
    if peso > gordo:
        gordo = peso
        codigoGordo = codigo
    if peso < magro:
        magro = peso
        codigoMagro = codigo

    contador += 1
    continuar = int(input("Se deseja parar digite 0: "))
    if continuar == 0:
        mediaAltura = somaAltura / contador
        mediaPeso = somaPeso / contador 
        print("Média de altura:", mediaAltura)
        print("Média de peso:", mediaPeso, "\n")
        print("Cliente mais alto:", maior,)
        print("Cliente mais baixo:", menor)
        print("Cliente mais gordo:", gordo)
        print("Cliente mais magro:", magro, "\n")
        print("Código do cliente mais alto", codigoMaior)
        print("Código do cliente mais baixo", codigoMenor)
        print("Código do cliente mais gordo", codigoGordo)
        print("Código do cliente mais magro", codigoMagro)
        break
    