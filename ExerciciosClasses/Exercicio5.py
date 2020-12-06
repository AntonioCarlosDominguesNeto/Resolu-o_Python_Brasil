'''
Exercicio 5: Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir 
os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, 
depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''
class contaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

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

conta1 = contaCorrente(1234, "Jair")
print(conta1.numeroConta, conta1.nomeCorrentista, conta1.saldo)
conta1.setNome("Luiza")
conta1.setNumero(4567)
conta1.setSaldo(1200)
print(conta1.numeroConta, conta1.nomeCorrentista, conta1.saldo)