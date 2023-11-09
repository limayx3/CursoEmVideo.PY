#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
#FAÇA UM PROGRAMA QUE AJUDE ELE LENDO O NOME DOS ALUNOS E ESCREVENDO O NOME DO ESCOLHIDO (MODULO RANDOM)
"""
1. Ler nome do aluno 1
2. Ler nome do aluno 2
3. Ler nome do aluno 3
4. Ler nome do aluno 4
5. Escolher um aluno randomicamente e exibir na tela
"""

import random
a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
#Ao invés de colocar o choice no print, da pra criar uma variável nova com ele e colocar essa variavel no print.
print('O aluno escolhido para apagar o quadro será: {}.'.format(random.choice(lista)))
