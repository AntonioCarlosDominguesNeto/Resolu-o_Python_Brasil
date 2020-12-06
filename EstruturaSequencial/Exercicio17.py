'''
Exercicio 17:
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
° comprar apenas latas de 18 litros;
° comprar apenas galões de 3,6 litros;
° misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
arredonde os valores para cima, isto é, considere latas cheias.
'''
metros = float(input("Digite quantos metros quadrados irão ser pintados: "))
litros = metros / 6
latas = int(litros / 18)
galoes = int(litros / 3.6)

if litros % 18 != 0:
    latas += 1
precoLatas = latas * 80

if galoes % 3.6 != 0:
    galoes += 1
precoGaloes = galoes * 25

latasComGaloes = int(litros / 18.0)
galoesComLatas = int((litros - (latasComGaloes * 18)) / 3.6)

if ((litros - (latasComGaloes * 18) % 3.6 != 0)):
    galoesComLatas += 1

precoFinal = (latasComGaloes * 80) + (galoesComLatas * 25)

print("Apenas latas, quantidade:", latas, ", preço: R$", precoLatas)
print("Apenas galões, quantidade:", galoes, ", preço: R$", precoGaloes)
print("Combinado, a quantidade de latas é de:", latasComGaloes, ", e de galões é:", galoesComLatas, ", e o preço: R$", precoFinal)