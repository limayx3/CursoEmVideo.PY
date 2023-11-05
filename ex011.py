#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, ONDE 1LITRO DE TINTA PINTA 2M²
"""
1. Ler altura da parede
2. Ler largura da parede
3. Calcular área da parede
4. Calcular quantos litros de tinta serão necessários
5. Exibir a quantidade de tinta que será necessária
"""

h = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
area = l * h
tinta = (area / 2)
print('Para esta parede que possui {:.2f}m² serão necessários {:.2f} litros de tinta.'.format(area, tinta))
