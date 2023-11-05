#CRIE UM ALGORÍTMO QUE LEIA UM NÚMERO E MOSTRE SEU DOBRO, TRIPLO E RAIZ QUADRADA:
"""
1. Ler um número
2. Calcular seu dobro
3. Calcular seu triplo
4. Calcular sua raiz quadrada
5. Exibir dobro, triplo e raiz quadrada
"""

n = float(input('Digite qualquer número: '))
d = n * 2
t = n * 3
r = n**(1/2)
print('Para {}, temos: \nSeu dobro é: {} \nSeu triplo é: {} \nSua raíz quadrada é: {}'.format(n, d, t, r))
