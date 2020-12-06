'''
Exercicio 40: Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de
trânsito. Foram obtidos os seguintes dados:
A. Código da cidade;
B. Número de veículos de passeio (em 1999);
C. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
D. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
E. Qual a média de veículos nas cinco cidades juntas;
F. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''
maior = 0
menor = 9999999999999999999999999999999999999
soma = 0 
somaMenor = 0
somaAcidentes = 0
contadorVeiculos = 0

for n in range(1, 6, 1):
    codigoCidade = int(input("Digite o cógigo da cidade: "))
    numeroVeiculos = int(input("Digite quantos veiculos: "))
    soma += numeroVeiculos
    acidentes = int(input("Digite o numero de acidentes: "))
    
    if acidentes > maior:
        maior = acidentes
        codigoMaior = codigoCidade
    
    if acidentes < menor:
        menor = acidentes
        codigoMenor = codigoCidade

    if numeroVeiculos < 2000: 
        somaAcidentes += acidentes
        contadorVeiculos += 1

mediaVeiculos = soma / 5
mediaAcidentes = somaAcidentes / contadorVeiculos

print("Maior indice de acidentes:", maior)
print("Código da cidade com maior indice de acidente:", codigoMaior, "\n")
print("Menor indice de acidentes:", menor)
print("Código da cidade com menor indice de acidente:", codigoMenor, "\n")
print("Média de veiculos das cidades:", mediaVeiculos)    
print("Média de acidentes com cidades que tem menos de 2000 veiculos:", mediaAcidentes)