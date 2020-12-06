'''
Exercicio 7: Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
A. Atributos: Nome, Fome, Saúde e Idade 
B. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome,Saúde e Idade Obs: Existe mais uma informação 
que devemos levar em consideração, o Humor do nosso tamagushi, estehumor é uma combinação entre os atributos 
Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação 
por que ela pode ser calculada a qualquer momento.
'''
class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

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

boneco1 = Tamagushi("Amigão", "Sem nenhuma fome", "Ótima", 1)
boneco2 = Tamagushi("Amigo", "Com um pouco de fome", "Boa", 3)
boneco3 = Tamagushi("Amiginho", "Morrendo de fome", "Péssima", 5)

print(boneco1.nome, boneco1.fome, boneco1.saude, boneco1.idade)
print("Humor:", boneco1.humor(boneco1.getFome, boneco1.getSaude))
print(boneco2.nome, boneco2.fome, boneco2.saude, boneco2.idade)
print("Humor:", boneco2.humor(boneco2.getFome, boneco2.getSaude))
print(boneco3.nome, boneco3.fome, boneco3.saude, boneco3.idade)
print(boneco3.humor(boneco3.getFome, boneco3.getSaude))