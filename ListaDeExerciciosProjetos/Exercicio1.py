'''
Exercicio 1: A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu 
servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço 
ocupado plos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da 
Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
'''
funcionarios = []
espacosDisponiveis = []
contador = 0
arquivo = open("funcionarios.txt", "r")
quantidade = arquivo.readlines()
arquivo.close()

for n in quantidade:
    quantidade = n.split()
    funcionarios.append(espacosDisponiveis[0])
    espacosDisponiveis.append(int(quantidade[1]))
contador = sum(espacosDisponiveis)

arquivoFinal = open("arquivoFinal.txt'", "w'")

for n in range(0, len(funcionarios)):
    espacoUso = espacosDisponiveis[n] / (1024 * 1024)
    percentualUso = espacosDisponiveis[n] / contador
    arquivoFinal.write(n + 1, funcionarios[n], "Espaço ocupado: ", espacoUso, "Percentual do uso: ", percentualUso / 100)

arquivoFinal.close()