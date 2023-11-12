#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE É PAR OU ÍMPAR.

num = int(input('Digite um número inteiro qualquer: '))
print('Você digitou o número {} e ele...'.format(num))
if (num % 2 == 0):
    print('... É PARRRRR!')
else:
    print('... mas bah, é ímpar tchê!')
