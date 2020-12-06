'''
Exercicio 20: Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a
média alcançada por aluno e presentar:
A. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
B. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
C. A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
m = (n1 + n2 + n3) / 3

print("Sua média foi igual a:", m)

if m == 10:
    print("Você foi aprovado com Distinção!")
elif m >= 7:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")