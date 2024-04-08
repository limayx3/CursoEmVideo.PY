#4 players rolam um dado e tenham resultados aleatórios. Guardá-los num dicionário e no fim mostrar em ordem, onde o ganhador tirou o maior.
#"O jogador 1 tirou X, o 2 tirou X,..." e "1º lugar o jogadorN com X, 2º lugar o jogadorN1 com X..."
from random import randint
from operator import itemgetter
from time import sleep

jogada = 0
rodada = {'jogador1':'', 'jogador2':'', 'jogador3':'', 'jogador4':''}

rodada['jogador1'] = randint(1, 6)
rodada['jogador2'] = randint(1, 6)
rodada['jogador3'] = randint(1, 6)
rodada['jogador4'] = randint(1, 6)
for k, v in rodada.items():
    print(f'{k} tirou {v}')

ranking = sorted(rodada.items(), key=itemgetter(1), reverse=True)
print(f'{' RaNkInG ':=^40}')
for i, n in enumerate(ranking):
    print(f' → Em {i+1}º temos o {n[0]} que tirou {n[1]}')
    sleep(0.5)
