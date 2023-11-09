#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
#(1) NOME TODO MAIÚSCULO, (2) NOME TODO MINÚSCULO, (3) TOTAL DE LETRAS FORA ESPAÇOS, (4) QTD LETRAS 1º NOME
"""
1. Ler nome completo
2. Exibir nome em maiúsculas
3. Exibir nome em minúsculas
4. Exibir total de letras excluindo os espaços
5. Exibir total de letras do primeiro nome
"""

nome = str(input('Informe seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
nospace = nome.replace(' ', '')
print(len(nospace))
dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(dividido[0], len(dividido[0])))
