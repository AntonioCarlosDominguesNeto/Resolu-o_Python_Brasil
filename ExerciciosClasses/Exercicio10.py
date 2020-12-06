'''
Exercicio 10: Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

A. tipoCombustivel.
B. valorLitro
C. quantidadeCombustivel

Possua no mínimo esses métodos:

A. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que 
foi colocada no veículo
B. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser 
pago pelo cliente.
C. alterarValor( ) – altera o valor do litro do combustível.
D. alterarCombustivel( ) – altera o tipo do combustível.
E. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
'''
class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valorLitro):
        self.valorLitro = valorLitro
        for n in range(0, self.valorLitro, 1):
            self.quantidadeCombustivel += 5

    def abastecerPorLitro(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel
        for n in range(0, quantidadeCombustivel, 1):
            self.valorLitro += 1

    def setTipo(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def getTipo(self):
        return self.tipoCombustivel

combustivel1 = bombaCombustivel("Gasolina", 5, 1)
combustivel1.abastecerPorValor(2)
print(combustivel1.tipoCombustivel, combustivel1.valorLitro, combustivel1.quantidadeCombustivel)