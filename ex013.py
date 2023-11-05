#FAÇA UM ALGORÍTMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO:
"""
1. Ler o salário atual
2. Calcular o novo valor acrescido de 15%
3. Exibir novo valor.
"""

v1 = float(input('Informe o valor atual do salário: R$'))
v2 = v1 * 1.15
print('O valor do salário acrescido de 15% é: R$ {:.2f}.'.format(v2))
