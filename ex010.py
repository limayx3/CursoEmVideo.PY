#CRIE UM PROGRAMA QUE LEIA QUANTO DINHERO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR, ONDE U$1,00 == R$3,27
"""
1. Ler valor na carteira
2. Calcular quantidade de dólares
3. Exibir quantos dólares compraria
"""

v = float(input('Informe quanta grana você tem disponível em reais: R$'))
print('{} reais compraria {:.2f} dólares à R$ 3,27 cada dólar.'.format(v, v/3.27))
