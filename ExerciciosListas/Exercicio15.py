'''
Exercicio 15:
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
A. Mostre a quantidade de valores que foram lidos;
B. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
C. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
D. Calcule e mostre a soma dos valores;
E. Calcule e mostre a média dos valores;
F. Calcule e mostre a quantidade de valores acima da média calculada;
G. Calcule e mostre a quantidade de valores abaixo de sete;
H. Encerre o programa com uma mensagem;
'''
quantidade = 0
nota = []
soma = 0
quantidadeValor = 0

while True:
    valor = float(input("Digite uma nota: "))
    soma += valor
    nota.append(valor)
    quantidade += 1
    continuar = int(input("Se deseja para digite um numero abaixo de 0: "))
    if continuar < 0:
        break
    
    if valor < 7:
        quantidadeValor += 1

media = soma / quantidade

print("Quantidade de notas:", quantidade)
print("Valores informados:", nota)
print("Valores inversos:", nota[::-1])
print("Soma dos valores:", soma)
print("Média dos valores:", media)
print("Quantidade de valor abaixo de 7:", quantidadeValor)
print("Programa encerrado")