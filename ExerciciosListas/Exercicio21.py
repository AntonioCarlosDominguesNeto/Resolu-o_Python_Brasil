'''
Exercicio 21: Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um 
desses carros faz com um litro de combustível. Calcule e mostre:
A. O modelo do carro mais econômico;
B. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 
quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela 
de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e 
podem mudar a cada execução do programa.
'''
carros = []
precos = []
maior = 0 
menor = 999999999999999999999
soma = 0

for n in range(1, 6, 1):
    carro = str(input("Digite um modelo de carro: "))
    carros.append(carro)
    preco = float(input("Digite o quanto custa o litro da gasolina:"))
    soma += preco
    rodado = int(input("Digite quantos kilometros ele roda com a gasolina:"))
    media = soma / rodado
    if media > maior:
        maior = media
    
    if media < menor:
        menor = media

print("Carros cadastrados:", carros)
print("Carro mais caro:", maior)
print("Carro mais barato:", menor)