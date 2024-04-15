#Programa com uma função chamada maior() que recebe vários valores inteiros como parâmetro e informa qual o maior.
'''Usando LISTA
def maior(list):
    vmaior = max(list)
    print(f'O maior valor é {vmaior} na(s) posição(ões): ', end="")
    for c in range (0, len(list)):
        if list[c] == vmaior:
            print(f'{c} ', end="")


vmaior = 0
números = []
while True:
    números.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'nN':
        print(números)
        maior(números)
        break
'''
from time import sleep

def maior(*num):
    cont = maior = 0
    print('~'*35)
    print(f'Analisando os valores ', end='')
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'\nForam analisados {cont} valores...', flush=True)
    sleep(0.5)
    print(f'Onde o maior valor informado foi {maior}.')


maior(4, 0, 4, 3, 1)
maior(-8, 8, 0, 4)
maior(0, 7, 5)