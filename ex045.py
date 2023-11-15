#CRIE UM PROGRAMA PARA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ E INFORMAR QUEM GANHOU.
"""
1. Ler nome do jogador
2. Apresentar as opções
3. Ler escolha do jogador
4. Randomizar própria escolha
5. Comparar a escolha do jogador com a própria
6. Informar quem ganhou
"""
import random

print('=' * 50)
print('{:=^50}'.format(' VAMOS JOGAR JOKENPÔ? '))
print('=' * 50)
opções = ('Pedra', 'Papel', 'Tesoura')
print('''O que você escolhe?
      0 - Pedra
      1 - Papel
      2 - Tesoura''')
user = int(input('Digite o número de sua escolha: '))
maq = random.randint(0, 2)
print('{: ^50}'.format(' JO... '))
print('{: ^50}'.format(' KEN... '))
print('{: ^50}'.format(' PÔ!!! '))
print('Eu: {}'.format(opções[maq]))
print('Você: {}'.format(opções[user]))

if maq == 0:
    if user == 0:
        print('EMPATAMOS! Vamo mais uma...')
    elif user == 1:
        print('VOCÊ VENCEU MIZERAVI!')
    elif user == 2:
        print('Eu vou te dar um fatality agora, perdedor!')
    else:
        print('Você é burro, sabe jogar não? Escolheu foi nada.')
elif maq == 1:
    if user == 0:
        print('HA! HA! VOCÊ PERDEU ZÉ RUELA!')
    elif user == 1:
        print('EMPATAMOS.')
    elif user == 2:
        print('VISH TU GANHOU!')
    else:
        print('Você é burro, sabe jogar não? Escolheu foi nada.')
elif maq == 2:
    if user == 0:
        print('AI ZÉ DA MANGA, TU GANHOU!')
    elif user == 1:
        print('Pai ta on, ganhei rapá!')
    elif user == 2:
        print('EMPATÊMO, agora vamo resolver no facão tche!')
    else:
        print('Você é burro, sabe jogar não? Escolheu foi nada.')