#Exercicio 6: Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
class tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def setCanal(self, canal):
        if self.canal <= 50 and self.canal >= 1:
            self.canal = canal

    def getCanal(self):
        return self.canal

    def setVolume(self, volume):
        if self.volume <= 100 and self.volume >= 0:
            self.volume = volume
        
    def getVolume(self):
        return self.volume

tv1 = tv(3, 55)
print(tv1.canal, tv1.volume)
tv1.setCanal(40)
tv1.setVolume(100)
print(tv1.canal, tv1.volume)