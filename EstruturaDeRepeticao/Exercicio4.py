'''
Exercicio 4: Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um 
programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale 
a população do país B, mantidas as taxas de crescimento.
'''
paisA = 80000
paisB = 200000
anosNecessarios = 0

while paisA < paisB:
    crescimentoA = paisA * 0.03
    crescimentoB = paisB * 0.015
    paisA += crescimentoA
    paisB += crescimentoB    
    anosNecessarios += 1

print("Anos necessarios:", anosNecessarios)
