#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E INDIQUE SE ELA POSSUI "SILVA" NO NOME.

nome = str(input('Digite o nome completo: ')).strip()
print('Esse nome possui "Silva"? ', 'SILVA' in nome.upper())
