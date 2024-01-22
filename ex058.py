#ESCREVA UM PROGRAMA QUE FAÇA O PC "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 10.
#PEÇA PARA O USUÁRIO DESCOBRIR QUAL FOI, DANDO OPÇÃO DE CHUTAR QUANTAS VEZES PRECISAR.
#O PROGRAMA DEVE INFORMAR SE ACERTOU OU NÃO E QUANTOS PALPITES FORAM NECESSÁRIOS PARA ACERTAR


import random
import time

n1 = random.randint(0, 10)
print('=' * 90)
print('Coé, duvido advinhar o número que eu pensei entre 0 e 10:')
print('=' * 90)
c = 0
n2 = int(input('Escreva sua escolha: '))
while n2 != n1:
    c += 1
    print('-' * 75)
    n2 = int(input('Eroooooou! Tente novamente: '))
print('=' * 90)
print('Acerou mizeravi, era {} mesmo.'.format(n1))
print('Mas é aquilo né, precisou de {} tentativas pra conseguir e só na {}ª deu bom kakaka.'.format(c, c+1))
print('=' * 90)


