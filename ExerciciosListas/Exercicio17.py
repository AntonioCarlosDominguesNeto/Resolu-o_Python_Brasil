'''
Exercicio 17: Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do 
atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e 
as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos 
saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
'''
saltos = []
nomes = []
soma = 0
contador = 0

while True:
    nome = str(input("Digite o nome do atleta: "))
    if nome in "":
        break
    else:
        nomes.append(nome)
        for n in range(1, 6, 1):
            salto = float(input("Digite a distancia do salto: "))
            soma += salto
            saltos.append(salto)
        print("\n")
        media = soma / 5
        contador += 1

for n in range(1, contador + 1, 1):
    print("Nome do competidor:", nomes[n - 1])
    print("Distancia do primeiro salto:", saltos[0])
    print("Distancia do segundo salto:", saltos[1])
    print("Distancia do terceiro salto:", saltos[2])
    print("Distancia do quarto salto:", saltos[3])
    print("Distancia do quinto salto:", saltos[4])
    print("Média dos saltos:", media)
    print("\n")