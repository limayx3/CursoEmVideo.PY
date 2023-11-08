#CRIE UM PROGRAMA QUE LEIA UM NÚERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA.
#EX: SE DIGITAR 5.098656, MOSTRAR APENAS O 5.
"""
1. Ler número real
2. Exibir apenas parte inteira
"""
import math
valor = float(input('Digite um número com casas decimais: '))
print('A porção inteira do valor digitado é {}.'.format(math.trunc(valor)))
