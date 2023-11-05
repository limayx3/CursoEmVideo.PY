#FAÇA UM ALGORÍTMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO:
"""
1. Ler o preço do produto
2. Calcular valor do produto -5%
3. Exibir valor do produto com desconto
"""

v1 = float(input('Digite o valor atual do produto: R$'))
v2 = v1 - (0.05 * v1)
print('O valor do produto com desconto de 5% é {} reais.'.format(v2))
