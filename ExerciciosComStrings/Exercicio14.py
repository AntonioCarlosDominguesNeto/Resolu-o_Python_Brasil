'''
Exercicio 14: Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em 
lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O 
uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada 
para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de 
traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
'''
traducao = {
    'A': '4',
    'B': '8',
    'C': '<',
    'D': '[)',
    'E': '&',
    'F': 'ph',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': 'j',
    'K': '|<',
    'L': '|_',
    'M': '|\/|',
    'N': '/\/',
    'O': '0',
    'P': '|*',
    'Q': '9',
    'R': 'l2',
    'S': '5',
    'T': '7',
    'U': 'v',
    'V': 'V',
    'W': 'vv',
    'X': '><',
    'Y': '`/',
    'Z': '2'
}

while True:
    string = str(input("Digite alguma coisa: "))

    for n in string.upper():
        if n.isalpha():
            print(traducao[n], end="")
        else:
            print ("\n")
        print("\n")

    continuar = str(input("Digite se deseja continuar[S/N]: ")).upper().strip()[0]
    if continuar in "N":
        break