#GERAR 5 NÚMEROS ALEATÓRIOS DE 0 À 10, EXIBIR TAL LISTA E INFORMAR QUAL MAIOR E QUAL MENOR VALORES.

from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('=*' * 15)
print(f'\nForam sorteados os valores: {números}. \n')
print(f'Dentre eles, temos que: \n{max(números)} é o maior valor. \n{min(números)} é o menor valor.')
print('=*' * 15)
