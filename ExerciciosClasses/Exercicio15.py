#Exercicio 15: Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
class Tamagushi:
    def __init__(self, nome, fome, saude, idade, comida=0, tempo=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.comida = comida
        self.tempo = tempo

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setFome(self, fome):
        self.fome = fome

    def getFome(self):
        return self.fome

    def setSaude(self, nome):
        self.saude = saude

    def getSaude(self):
        return self.saude

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

    def humor(self, fome, saude):
        if self.fome in "Sem nenhuma fome" and self.saude in "Ótima":
            print("Feliz")
        elif self.fome in "Com um pouco de fome" and self.saude in "Boa":
            print("Ok")
        else:
            print("Descontente")

    def darComida(self, comida):
        if self.comida in str:
            fome = "Sem nenhuma fome"

    def tempoBrncar(self, tempo):
        if self.tempo > 1:
            saude = "Ótima"