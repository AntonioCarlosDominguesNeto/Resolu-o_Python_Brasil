#Exercício 7: Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
base = float(input("Digite a base do quadrado: "))
altura = float(input("Digite a altura do quadrado: "))
area = base * altura
dobro = area * 2

print("A area é de:", area,"Cm²")
print("O dobro dessa area é:", dobro,"Cm²")