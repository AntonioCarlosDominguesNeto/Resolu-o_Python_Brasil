'''
Exercicio 16: Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores 
exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, 
for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.
'''
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

    def str(self):
        print("Nome:", self.getNome())
        print("Idade:", self.getIdade())
        print("Fome:", self.getFome())
        print("Saude:", self.getSaude())
        print("Humor:", self.humor())