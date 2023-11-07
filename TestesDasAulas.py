"""Aula 06
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
print('A soma entre {} e {} é igual à: {}.'.format(n1, n2, s))
"""
"""Aula 07
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
print('As operações realizadas com {} e {} são: \nSoma: {:>30}\nSubtração: {:>30}\nMultiplicação: {:>30}\nDivisão: {:>30.2f}\nPotência: {:>30}'.format(n1, n2, s, su, m, d, p))
"""
"""Aula 08

import math
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz quadrada de {} é {:.2f}.'.format(n, raiz))


from math import sqrt, floor
n = int(input('Digite um número: '))
raiz = sqrt(n)
print('A raíz quadrada de {} é {:.2f}.'.format(n, floor(raiz)))
"""
import emoji
print(emoji.emojize('Olá :Brazil:', language='alias'))
