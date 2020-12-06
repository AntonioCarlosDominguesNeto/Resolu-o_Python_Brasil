'''
Exercicio 11: Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
A. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível 
no tanque.
B. O consumo é especificado no construtor e o nível de combustível inicial é 0.
C. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível 
de combustível no tanque de gasolina.
D. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
E. Forneça um método adicionarGasolina( ), para abastecer o tanque. 
'''
class carro():
    def __init__(self, quantidade, consumo = 0):
        self.consumo = consumo
        self.quantidade = quantidade


    def andar(self, distancia):
        gasto = self.consumo / distancia 
        self.quantidade -= gasto

    def obterGasolina(self, quantidade):
        self.quantidade = quantidade
        for n in range(0, self.quantidade, 1):
            self.quantidade += 2

c1 = carro(100, 0)
c1.andar(100)
print(c1.andar(100), c1.quantidade)