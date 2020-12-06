'''
Exercicio 17: Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles 
através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta 
de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o 
usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os 
bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um 
nivel inicial aleatório de fome e tédio.
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