'''
Exercicio 8: Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo 
menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos 
dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada 
refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
'''
class macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def digerir(self, bucho):
        self.bucho.pop(0)

macaco1 = macaco("Fulano", "Maçã")
macaco1.comer("Tomate")
macaco2 = macaco("Ciclano", "Banana")
macaco2.comer("Abacaxi")
print(macaco1.nome, macaco1.bucho)
print(macaco2.nome, macaco2.bucho)