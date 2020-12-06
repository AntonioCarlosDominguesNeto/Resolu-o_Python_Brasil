'''
Exercicio 46:
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de 
cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores 
restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus 
saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior 
salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na 
ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do 
atleta.
'''
maior = 0
menor = 999999999999999999999999999999999999999
soma = 0 
for n in range(1, 6, 1):
    salto = float(input("Digite a distancia do salto(digite sue maior e menor nota primeiro): "))
    
    if salto > maior:
        maior = salto
        salto = 0     
    elif salto < menor:
        menor = salto
        salto = 0
    else:
        soma += salto

media  = soma / 3
print("Maior salto:", maior)
print("Menor salto", menor)
print("Média:", media)