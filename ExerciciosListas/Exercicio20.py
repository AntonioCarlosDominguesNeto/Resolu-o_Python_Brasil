#Exercicio 20: As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom ]resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
salarios = []
abono = 0.0
contador = 0
maior = 0

while True:
    salario = float(input("Digite o salário: "))
    if salario < 0:
        break
    else:
        salarios.append(salario)

for n in salarios:
    bonus = salario * 0.2
    if bonus < 100:
        bonus = 100.0
        contador += 1
    maior += abono
    if bonus > maior:
        maior = bonus

print("Salario normal:", salarios)
print("Abono:", maior)