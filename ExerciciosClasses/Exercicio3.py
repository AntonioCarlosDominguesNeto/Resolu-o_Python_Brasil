'''
Exercicio 3: Classe Retangulo: Crie uma classe que modele um retangulo:
A. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
B. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
C. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o 
local.
'''
class retangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def setLados(self, altura):
        self.altura = altura
    
    def getLados(self):
        return self.altura
    
    def calcularArea(self):
        return self.altura * self.base

    def calcularPelimetro(self):
        return 2 * (self.altura + self.base)

retangulo1 = retangulo(4, 7)
print(retangulo1.calcularArea())
print(retangulo1.calcularPelimetro())
retangulo1.setLados(5)
print(retangulo1.calcularArea())
print(retangulo1.calcularPelimetro())