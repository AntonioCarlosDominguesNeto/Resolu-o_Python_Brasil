#Exercicio 25: Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
quantidadeAlunos = int(input("Digite a quantidade de alunos que serão registrados: "))
soma = 0

for n in range(1, quantidadeAlunos + 1, 1):
    idade = int(input("Digite a sua idade: "))
    soma = soma + idade

media = soma / quantidadeAlunos
print("A média é:", media)

if media >= 0 and media <= 25:
    print("A turma é jovem!")
elif media >= 26 and media <= 60:
    print("A turma é adulta!")
elif media > 60:
    print("A turma é idosa!")
else:
    print("Numeros invalidos!")