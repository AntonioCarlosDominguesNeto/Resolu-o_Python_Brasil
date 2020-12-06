'''
Exercicio 3: Faça um programa que leia e valide as seguintes informações:
A. Nome: maior que 3 caracteres;
B. Idade: entre 0 e 150;
C. Salário: maior que zero;
D. Sexo: 'f' ou 'm';
E. Estado Civil: 's', 'c', 'v', 'd';
'''
while True:
    nome = str(input("Digite o seu nome: "))
    if len(nome) > 3:
        idade = int(input("Digite a sua idade: "))
        if idade >= 0 and idade <= 150:
            salario = float(input("Digite o seu salário: "))
            if salario > 0:
                sexo = str(input("Digite o seu sexo[M/F]: ")).upper().split()[0]
                if sexo in "MF":
                    estadoCivil = str(input("Digite seu estado civil[S/C/V/P]: ")).upper().split()[0]
                    if estadoCivil in "SCVP":
                        print("Nome registrado:", nome)
                        print("Idade registrada:", idade)
                        print("Salário registrado:", salario)
                        print("Sexo registrado:", sexo)
                        print("Estado civil registrado:", estadoCivil)
                        break
                    else:
                        print("Estado civil invalido!")
                else:
                    print("Sexo invalido!")
            else:
                print("Salário invalido!")
        else:
            print("Idade invalida!")
    else:
        print("Nome invalido!")