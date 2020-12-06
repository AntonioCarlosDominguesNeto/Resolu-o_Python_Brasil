#Exercicio 33: O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
numero = int(input("Digite quantas temperaturas irá registrar: "))
maior = 0 
menor = 99999999999999999999999999999999999999999999999
soma = 0

for n in range(1, numero + 1, 1):
    temperatura = float(input("Digite a temperatura: "))
    soma += temperatura
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura

media = soma / numero

print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
print("Media das temperaturas:", media)