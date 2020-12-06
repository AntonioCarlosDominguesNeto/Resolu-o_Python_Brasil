#Exercicio 1: Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
string1 = str(input("Digite a primeira string: "))
string2 = str(input("Digite a segunda string: "))
print("Tamanho da primeira string:", len(string1))
print("Tamanho da segunda string:", len(string2))
if len(string1) == len(string2):
    print("As duas têm o mesmo tamanho.")
else:
    print("As duas têm tamanhos diferentes.")