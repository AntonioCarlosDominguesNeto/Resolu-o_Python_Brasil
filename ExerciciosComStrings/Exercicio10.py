#Exercicio 10: Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
numeroExtenso = ["Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete","Dezoito", "Dezenove", "Vinte", "Vinte e um", "Vinte e dois", "Vinte e três", "Vinte e quatro", "Vinte e cinco", "Vinte e seis", "Vinte e sete", "Vinte e oito", "Vinte e nove", "Trinta", "Trinta e um", "Trinta e dois", "Trinta e três", "Trinta e quatro", "Trinta e cinco", "Trinta e seis", "Trinta e sete","Trinta e oito", "Trinta e nove", "Quarenta", "Quarenta e um", "Quarenta e dois", "Quarenta e três", "Quarenta e quatro", "Quarenta e cinco", "Quarenta e seis", "Quarenta e sete", "Quarenta e oito", "Quarenta e nove", "Cinquenta", "Cinquenta e um", "Cinquenta e dois", "Cinquenta e três", "Cinquenta e quatro", "Cinquenta e cinco", "Cinquenta e seis", "Cinquenta e sete", "Cinquenta e oito", "Cinquenta e nove", "Sessenta", "Sessenta e um", "Sessenta e dois", "Sessenta e três", "Sessenta e quatro", "Sessenta e cinco", "Sessenta e seis", "Sessenta e sete", "Sessenta e oito", "Sessenta e nove", "Setenta", "Setenta e um", "Setenta e dois", "Setenta e três", "Setenta e quatro", "Setenta e cinco", "Setenta e seis", "Setenta e sete", "Setenta e oito", "Setenta e nove", "Oitenta", "Oitenta e um", "Oitenta e dois", "Oitenta e três", "Oitenta e quatro", "Oitenta e cinco", "Oitenta e seis", "Oitenta e sete", "Oitenta e oito", "Oitenta e nove", "Noventa", "Noventa e um", "Noventa e dois", "Noventa e três", "Noventa e quatro", "Noventa e cinco", "Noventa e seis", "Noventa e sete", "Noventa e oito", "Noventa e nove"]
numero = int(input("Digite um numero de 1 a 99: "))

if numero > 99 or numero < 1:
    print("Numero inválido!")
else:
    print("Numero por extenso:", numeroExtenso[numero - 1])