#Exercicio 4: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra: ").upper().split()[0]

if letra in "AEIOU":
    print("A letra", letra,", é uma vogal")
else:
    print("A letra", letra, ", é uma consoante")