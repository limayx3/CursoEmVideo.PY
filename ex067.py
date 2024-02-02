#MOSTRAR TABUADA DO NÚMERO QUE A PESSOA ESCOLHER, PARA CADA VALOR DIGITADO PELO USER.
#PROGRAMA É INTERROMPIDO QUANDO NÚMERO DIGITADO FOR NEGATIVO.

n = 0
c = 1

while True:
    n = int(input('\nDigite o número que quer saber a tabuada (valor negativo para parar): '))
    if n < 0:
        break
    print('=' * 25)
    print(f'Tabuada de {n}:')
    print('='* 25)
    for c in range (1, 11):
        print(f'{n:>6} x {c:^2} = {n*c}')
        c += 1
    print('='* 25)
print('PrOgRaMa FiNaLiZaDo.\n')
