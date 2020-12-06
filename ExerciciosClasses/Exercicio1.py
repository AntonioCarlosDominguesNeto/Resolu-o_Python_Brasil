'''
Exercicio 1: Classe Bola: Crie uma classe que modele uma bola:
A. Atributos: Cor, circunferência, material
B. Métodos: trocaCor e mostraCor
'''
class bola:    
    def __init__(self, cor, material, circunferencia):
        self.cor = cor
        self.material = material 
        self.circunferencia = circunferencia  

    def mudarCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)

bola1 = bola("Azul", "Borracha", "0.66")
print(bola1.cor, bola1.material, bola1.circunferencia)
bola1.mudarCor("Branco")
print(bola1.cor)