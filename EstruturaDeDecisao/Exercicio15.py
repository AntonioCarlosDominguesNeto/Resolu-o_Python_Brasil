#Exercicio 15: Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
triangulo1 = float(input("Digite o lado do triangulo: "))
triangulo2 = float(input("Digite o lado do triangulo: "))
triangulo3 = float(input("Digite o lado do triangulo: "))

if(triangulo1 == triangulo2 == triangulo3):
    print("Equilatero")
elif(triangulo1 == triangulo2 or triangulo1 == triangulo3 or triangulo2 == triangulo3):
    print("Isósceles")
else:
    print("Escaleno")