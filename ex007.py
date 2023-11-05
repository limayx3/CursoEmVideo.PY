#DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA:
"""
1. Ler nota n1
2. Ler nota n2
3. Calcule média entre n1 e n2
4. Exiba média do aluno
"""

aluno = input('Qual nome do aluno? ')
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
print('A média de {} é {}.'.format(aluno, m))
