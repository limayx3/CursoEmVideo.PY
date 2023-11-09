#faça um programa que leia o nome completo de uma pessoa, indicando qual é seu primeiro e último nome respectivamente.

nome = str(input('Digite o nome completo: ')).strip()
print('Seu nome completo é {}.'.format(nome))
split = nome.split()
first = split[0].title()
last = split[-1].title()
print('O primeiro nome é {} e o último {}.'.format(first, last))
