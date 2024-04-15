#Criar a função contador() que recebe início, fim e passo. Realizar 3 contagens de uma vez:
# A de 1 à 10 de 1 em 1; B de 10 à 0 de 2 em 2; C a contagem personalizada
from time import sleep

def linha():
    print('~' * 30)

def contador(i, f, p):
    linha()
    print('Contagem A → ', end="")
    for c in range(1, 10):
        print(f'{c} ', end="", flush=True)
        sleep(0.5)
    print('')
    linha()
    print('Contagem B → ', end="")
    for c in range (10, -1, -2):
        print(f'{c} ', end="", flush=True)
        sleep(0.5)
    print('')
    linha()
    print('Contagem C → ', end="")
    if i > f:
        for c in range(i, f+1, -p):
            print(f'{c} ', end="", flush=True)
            sleep(0.5)
    else:
        for c in range(i, f+1, p):
            print(f'{c} ', end="", flush=True)
            sleep(0.5)


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
