'''
Exercicio 2: Classe Quadrado: Crie uma classe que modele um quadrado:
A. Atributos: Tamanho do lado
B. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''
class quadrado:
    def __init__(self, tamanho, lado):
        self.tamanho = tamanho
        self.lado = lado
    
    def setLado(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado

    def calculaArea(self):
        return self.lado * self.tamanho

quadrado1 = quadrado(5, 7)
print(quadrado1.lado, quadrado1.tamanho)
print(quadrado1.calculaArea())
quadrado1.setLado(5)
print(quadrado1.calculaArea())