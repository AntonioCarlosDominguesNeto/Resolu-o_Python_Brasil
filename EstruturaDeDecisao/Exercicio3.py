#Exercicio 3: Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input("Digite o seu sexo[M/F]: ").upper().split()[0]

if sexo in "M":
    print("Você é do sexo masculino")
elif sexo in "F":
    print("Você é do sexo feminino")
else:
    print("Opção invalída")
