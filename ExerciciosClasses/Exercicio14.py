#Exercicio 14: Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, aumento):
        self.salario = self.salario * (aumento / 100)
        self.salario = self.salario + aumento
        return self.salario

f1 = funcionario("Marcos", 1500)
print(f1.nome, f1.salario)
print(f1.aumentarSalario(10))