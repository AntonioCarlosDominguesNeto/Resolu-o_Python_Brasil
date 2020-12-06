'''
Exercicio 12: Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe 
contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure 
tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que 
adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma 
taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
'''
class contaInvestimento:
    def __init__(self, numeroConta, nomeCorrentista, saldo=0, taxaJuros=10):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def setNumero(self, numeroConta):
        self.numeroConta = numeroConta
    
    def getNumero(self):
        return self.numeroConta

    def setNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def getNome(self):
        return self.nomeCorrentista

    def setSaldo(self, saldo):
        self.saldo = saldo
    
    def getSaldo(self):
        return self.saldo

    def adicioneJuros(self, taxaJuros):
        self.taxaJuros = taxaJuros

    