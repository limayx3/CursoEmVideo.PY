#O PROFESSOR QUER SORTEAR A ORDEM DE APRESENTAÇO DOS TRABALHOS DOS 4 ALUNOS.
#FAÇA UM PROGRAMA QUE LEIA SEUS NOMES E MOSTRE A ORDEM DE APRESENTAÇÃO
"""
1. Ler nome do aluno 1
2. Ler nome do aluno 2
3. Ler nome do aluno 3
4. Ler nome do aluno 4
5. Exibir os nomes em ordem aleatórea para apresentação
"""

import random
a1 = input('Informe o nome do 1º aluno: ')
a2 = input('Informe o nome do 2º aluno: ')
a3 = input('Informe o nome do 3º aluno: ')
a4 = input('Informe o nome do 4º aluno: ')
lista = [a1, a2, a3, a4]
#Da pra usar o "random.shuffle(lista)" também, além de poder colocar ele fora do print
print('A ordem de apresentação dos trabalhos será:\n {}.'.format(random.sample(lista, k=4)))
