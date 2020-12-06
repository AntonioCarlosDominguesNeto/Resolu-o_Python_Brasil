'''
Exercicio 14: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de
um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
'''
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
notaLetra = "Nota inválida!"

if media >= 9 and media <= 10:
    notaLetra = "A"
elif media >= 7.5 and media <= 8.9:
    notaLetra = "B"
elif media >= 6 and media <= 7.4:
    notaLetra = "C"
elif media >= 4 and media <= 5.9:
    notaLetra = "D"
elif media >= 0 and media <= 3.9:
    notaLetra = "E"
else:
    print("Nóta inválida!")

print("Sua nota foi:", notaLetra)

if notaLetra in "ABC":
    print("Aprovado!")
else:
    print("Reprovado!")