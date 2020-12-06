'''
Exercicio 24: Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os 
resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores
(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
'''
import random

dados = []
for n in range(1, 101, 1):
    dado = random.randint(1, 6)
    dados.append(int(dado))

print("Resultado dos dados:", dados)