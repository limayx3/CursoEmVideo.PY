#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SEU SUCESSOR E SEU ANTECESSOR:
"""
1. Ler número inteiro
2. Calcular sucessor
3. Calcular antecessor
4. Exibir sucessor e antecessor
"""

n = int(input('Digite um número inteiro: '))
s = n + 1
a = n - 1
print('O sucessor de {} é {}, já seu antecessor é {}.'.format(n, s, a))
