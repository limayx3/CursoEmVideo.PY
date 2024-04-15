#Faça um programa com a lista números e crie duas funções: sorteia() que sorteará 5 números, incluindo-os na lista.
#Então a função somaPar() que mostre a soma entre os números pares sorteados
from random import randint

def sorteia(list):
    for c in range (0, 5):
        list.append(randint(0, 10))

def somaPar(list):
    soma = 0
    for c, v in enumerate(list):
        if v % 2 == 0:
            soma += v
    print(f'A soma dos pares da lista {list} é {soma}.')


valores = []
sorteia(valores)
somaPar(valores)
