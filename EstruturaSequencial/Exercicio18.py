#Exercicio 18: Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho = int(input("Informe o tamanho do arquivo em MB: "))
velocidade = int(input("Informe a velocidade de sua internet em Mbps: "))
bits = tamanho * 1024 * 2 * 8 
tempo = (bits / (velocidade * 1024 * 2)) / 60

print("O tempo em minutos será de:", tempo)