#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 À 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS CONFORME:
#(1) MILHAR, (2) CENTENA (3) DEZENA, (4) UNIDADE                            OBS: COMO STRING E COMO NÚMERO
"""
1. Ler número com 4 dígitos
2. Mistrar qual é milhar, centena, dezena e unidade
"""
"""num = str(input('Informe um número com 4 algarismos: '))
print('O número digitado foi {} e nele, temos:'.format(num))
print('O milhar é: ', num[0])
print('A centena é: ', num[1])
print('A dezena é: ', num[2])
print('A unidade é: ', num[3])"""

numeral = int(input('Digite um número até 4 algarismos: '))
u = numeral // 1 % 10
d = numeral // 10 % 10
c = numeral // 100 % 10
m = numeral // 1000 % 10
print('\nJá para o número {}, temos:'.format(numeral))
print('O milhar é: {}'.format(m))
print('A centena é: {}'.format(c))
print('A dezena é: {}'.format(d))
print('A unidade é: {}'.format(u))
