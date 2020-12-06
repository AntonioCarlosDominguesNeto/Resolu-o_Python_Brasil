'''
Exercicio 18: Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber 
qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será 
utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este 
programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, 
entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a 
votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve 
mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
A. O total de votos computados;
B. Os númeos e respectivos votos de todos os jogadores que receberam votos;
C. O percentual de votos de cada um destes jogadores;
D. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o 
percentual de votos dados a ele.
'''
votos = [0] * 23
voto = -1
contador = 0
contador2 = 1
vencedor = 0

while True:
    voto = int(input('Numero do jogador[0 até 23]: '))
    if voto == 0 or voto > 23:
        print("Valor inválido!")
    elif voto < 0:
        break
    else:
        votos[0] += 1
        if votos[contador] > vencedor:
            vencedor = votos[contador]
        contador += 1

print("Total de votos:", contador)
print("Vencedor:", vencedor)