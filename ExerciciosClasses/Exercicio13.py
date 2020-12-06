#Exercicio 13: Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. 
class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

f1 = funcionario("Marcos", 1500)
print(f1.nome, f1.salario)