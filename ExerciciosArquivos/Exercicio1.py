#Exercicio 1: Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
ipsValidos = []
ipsInvalidos = []
ips = []

def validacao():
    while True:
        ip = str(input("Digite um endereço de ip: "))
        tamanho = len(ip)
        if tamanho != 13:
            ipsInvalidos.append(ip)
        else:        
            for n in range(1, tamanho + 1, 1):
                ips.append(ip[n - 1])
            
            if tamanho > 13 or tamanho < 0:
                ipsInvalidos.append(ip)
            elif ips[0] not in "12"  and ips[2] not in "12345" or ips[10] not in "12" and ips[12] not in "12345":
                ipsInvalidos.append(ip)
            elif ips[3] != "." or ips[7] != "." or ips[9] != ".":
                ipsInvalidos.append(ip)
            else:
                ipsValidos.append(ip)
            
        continuar = str(input("Deseja continuar[S/N]: ")).upper().strip()[0]
        if continuar in "N":
            print("Ips Válidos:", ipsValidos)
            print("Ips Inválidos:", ipsInvalidos)
            break
        else: 
            ips.clear()

validacao()