#Programa deve perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo (na quantidade especificada),
#cadastrando tudo em uma única lista composta. Adicionar timer ao printar cada um dos jogos sorteados.

from random import sample
from time import sleep
jogos = list()
novo = list()

quant = int(input('Quantos jogos deseja sortear? '))
for c in range (0, quant):
    novo = sample(range(1, 61), 6)
    jogos.append(novo)
print('Gerando jogos ganhadores...')
sleep(1)
print(f'{" LISTA DE JOGOS ":=^40}')
for pos, j in enumerate(jogos):
    sleep(0.5)
    print(f'{(pos+1):>3}º JOGO: {sorted(j)}')
print(f'{" FIM DA LISTA ":=^40}')
