'''
#Exercicio 4: Classe Pessoa: Crie uma classe que modele uma pessoa:
A. Atributos: nome, idade, peso e altura
B. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''
class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1

    def engordar(self):
        self.peso += 1

    def emagrecer(self):
        self.peso -= 1

    def crescer(self):
        if self.idade <= 21:
            self.altura += 0.05
        else:
            self.idade += 0

pessoa1 = pessoa("Luiz", 19, 68, 1.73)
pessoa2= pessoa("Carlos", 22, 70, 1.80)
pessoa1.engordar()
pessoa1.crescer()
print(pessoa1.peso, pessoa1.altura)
pessoa2.crescer()
pessoa2.emagrecer()
print(pessoa2.peso, pessoa2.altura)