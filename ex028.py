#ESCREVA UM PROGRAMA QUE FAÇA O PC "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 5.
#PEÇA PARA O USUÁRIO DESCOBRIR QUAL FOI.
#O PROGRAMA DEVE INFORMAR SE ACERTOU OU NÃO.
"""
1. Programa gera um número aleatório de 0 à 5
2. Ler número do usuário
3. Informar se acertou
4. Informar se errou
"""
import random
import time
n1 = random.randint(0,5)
print('-' * 67)
print(' Olá, tente acertar qual foi o algarismo de 0 à 5 que eu pensei! ')
print('-' * 67)
n2 = int(input('Digite um algarismo de 0 à 5: '))
print('-' * 67)
print('\nPROCESSANDO...')
time.sleep(3) #Comando para esperar 3 segundos antes de dar a resposta
if n2 == n1:
    print('Acertou mizeravi! Eu pensei em {}! Agora joga na mega sena!'.format(n1))
else:
    print('Eroooooooou! Você não tem as manha, eu pensei em {}.'.format(n1))
print('-' * 67)
