#ESCREVA UM PROGRAMA QUE LEIA 2 NÚMEROS INTEIROS E COMPARE-OS INFORMANDO:
#(1) O 1º VALOR É MAIOR, (2) O 2º VALOR É MAIOR, (3) NÃO EXISTE VALOR MAIOR, ELES SÃO IGUAIS.
"""
1. Ler número inteiro
2. Comparar qual é o maior e informar
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número ({}) é maior que o segundo ({}).'.format(n1, n2))
elif n2 > n1:
    print('O segundo número ({}) é maior que o primeiro ({}).'.format(n2, n1))
else:
    print('Os valores digitados são iguais ({} e {}).'.format(n1, n2))

print('Fique com Deus.')
