#Exercicio 5: Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
populaçãoA = int(input("Digite a população do primeiro pais: "))
taxaA = int(input("Digite a taxa de crescimento do primeiro pais: "))
populaçãoB = int(input("Digite a população do segundo pais: "))
taxaB = int(input("Digite a taxa de crescimento do segundo pais: "))
anosNecessarios = 0

if populaçãoA > populaçãoB:
    if taxaA < taxaB:
        while populaçãoB < populaçãoA:
            populaçãoA = populaçãoA + (populaçãoA * taxaA) / 100
            populaçãoB = populaçãoB + (populaçãoB * taxaB) / 100
            anosNecessarios += 1
        print("Anos Necessarios:", anosNecessarios)
    elif taxaA > taxaB:
        print("Me desculpe, mas como a população 'A' já é maior que a 'B' você não pode colocar uma taxa de crescimento maior ou igual para ela")         

if populaçãoB > populaçãoA:
    if taxaA > taxaB:
        while populaçãoB > populaçãoA:
            populaçãoA = populaçãoA + (populaçãoA * taxaA) / 100
            populaçãoB = populaçãoB + (populaçãoB * taxaB) / 100
            anosNecessarios += 1
        print("Anos Necessarios:", anosNecessarios)
        print("Me desculpe, mas como a população 'A' já é menor que a 'B' você não pode colocar uma taxa de crescimento maior ou igual para ela") 
    elif taxaA < taxaB:
        print("Me desculpe, mas como a população 'A' já é menor que a 'B' você não pode colocar uma taxa de crescimento maior ou igual para ela") 

if populaçãoA == populaçãoB:
    print("Ambos já tem a mesma população, não será necessario o calculo")
else:
    print("Você não digitou corretamente!")
