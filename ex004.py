digitado = input('Digite alguma coisa, creatino: ')
print('O tipo primitivo é {}.'.format(type(digitado)))
'''
print('É um número? ', digitado.isnumeric())
print('É só texto? ', digitado.isalpha())
print('Só tem espaços? ', digitado.isspace())
print('É alphanumérico? ', digitado.isalnum())
print('Está capitalizado? ', digitado.istitle())
print('Está todo em maiúsculas? ', digitado.isupper())
print('Está todo em minúsculas? ', digitado.islower())
'''

print('Numeral: {}'.format(digitado.isnumeric()))
print('Apenas texto: {}'.format(digitado.isalpha()))
print('Apenas espaços: {}'.format(digitado.isspace()))
print('Alphanumerico: {}'.format(digitado.isalnum()))
print('Capitalizado: {}'.format(digitado.istitle()))
print('Apenas maiúsculas: {}'.format(digitado.isupper()))
print('Apenas minúsculas: {}'.format(digitado.islower()))