#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ESTEVE ALUGADO.
#CALCULE O PREÇO A PAGAR, SENDO O PREÇO R$60,00 POR DIA E R$0,15 POR KM
"""
1. Ler quantidade de kms rodados
2. Ler quantidade de dias alugado
3. Calcular preço
4. Exibir preço a pagar pelo aluguel
"""

km = float(input('Informe quantos quilômetros percorreu com o veículo: '))
d = float(input('Informe quantos dias este veículo ficou sobre sua posse: '))
p = (km * 0.15) + (d * 60)
print('Por {}km rodados em {} dias, você precisa pagar: R${:.2f}.'.format(km, d, p))
