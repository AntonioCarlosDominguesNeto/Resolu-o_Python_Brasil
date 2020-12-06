'''
Exercicio47: Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota 
são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o 
nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua 
média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as 
notas restantes). As notas não são informados ordenadas.
'''
maior = 0
menor = 999999999999999999999999999999999999999
soma = 0 
for n in range(1, 8, 1):
    salto = float(input("Digite a distancia do salto(digite sue maior e menor nota primeiro): "))
    
    if salto > maior:
        maior = salto
        salto = 0     
    elif salto < menor:
        menor = salto
        salto = 0
    else:
        soma += salto

media  = soma / 5
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média:", media)