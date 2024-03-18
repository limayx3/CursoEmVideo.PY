#4 players rolam um dado e tenham resultados aleatórios. Guardá-los num dicionário e no fim mostrar em ordem, onde o ganhador tirou o maior.
#"O jogador 1 tirou X, o 2 tirou X,..." e "1º lugar o jogadorN com X, 2º lugar o jogadorN1 com X..."
from random import randint

jogada = 0
rodada = {'jogador1':'', 'jogador2':'', 'jogador3':'', 'jogador4':''}
decrescente = {}

rodada['jogador1'] = randint(1, 6)
rodada['jogador2'] = randint(1, 6)
rodada['jogador3'] = randint(1, 6)
rodada['jogador4'] = randint(1, 6)

print(sorted(rodada.items(), reverse=True))
for k, v in sorted(rodada.items(), reverse=True):
    print(f'{k} = {v}')