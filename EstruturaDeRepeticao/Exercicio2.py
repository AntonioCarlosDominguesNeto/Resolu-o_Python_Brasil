#Exercicio 2: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    usuario = input("Digite o seu usuario: ")
    senha = input("Digite a sua senha: ")
    if senha in usuario:
        print("Senha invalida, pois é igual ao nome de usuario")
    else:
        print("Usuario e senha cadastrados!")
        break