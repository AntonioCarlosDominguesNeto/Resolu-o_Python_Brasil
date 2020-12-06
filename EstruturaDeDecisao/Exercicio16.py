'''
Exercicio 16: Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O
programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes 
situações:
A. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
pedir os demais valores, sendo encerrado;
B. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o
programa;
C. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
D. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Não é uma equação de segundo grau!")
else:
    delta = math.pow(b, 2) - (4 * a * c)
    if delta == 0:
        r = -(b) / (2 * a)
        print("A equação só têm uma raiz")
        print("A raiz é:", r)
    elif delta < 0:
        print("Essa equação não tem valores reais")
    else:
        r1 = (-(b) + math.sqrt(delta)) / (2 * a)
        r2 = (-(b) - math.sqrt(delta)) / (2 * a)
        print("Essa equação têm duas raizes")
        print("A primeira é:", r1)
        print("A segunda é:", r2)