#JOGAR PAR OU ÍMPAR COM O PC, INTERROMPENDO QUANDO O USER PERDER.
#AO FINDAR, MOSTRAR TOTAL DE VITÓRIAS DO USER.

import random
import time

player1 = player2 = count = soma = 0

while True:
    print('=' * 100)
    player1 = int(input('Escolha um número inteiro de 0 à 10: '))
    player2 = random.randint(0,10)
    soma = player1 + player2
    escolha = str(input('"p" para par ou "i" para ímpar? ')).strip().lower()[0]
    for c in range (1, 4):
        time.sleep(0.5)
        print(f'{c}...')


    if escolha == 'p':
        if soma % 2 != 0:
            break
        else:
            print(f'Deu PAR!\n')
            count += 1        
    elif escolha == 'i':
        if soma % 2 == 0:
            break
        else:
            print(f'Deu ÍMPAR!\n')
            count += 1
            
print('=' * 100)
print(f'Xiiiiii....... Deu ruim após {count} vitórias, meu consagrado.')
print('=' * 100)
