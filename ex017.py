#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DOS CATETOS OPOSTO E ADJACENTE DE UM TRIÂNGULO RETÂNGULO E CALCULE/ MOSTRE A HIPOTENUSA.
#QUADRADO DA HIPOTENUSA = SOMA DOS QUADRADOS DOS CATETOS (MAS TEM FUNÇÃO QUE FAZ)
"""
1. Ler cateto oposto
2. Ler cateto adjacente
3. Mostrar hipotenusa
"""

import math
co = float(input('Informe o cateto oposto (apenas números): '))
ca = float(input('Informe o cateto adjacente (apenas números): '))
#Para calcular a HIpotenusa sem a importação da biblioteca, basta fazer isso e o valor de hi ser exibido como hipotenusa.
#hi = (co ** 2 + ca ** 2) ** (1/2) 
print('Para os catetos oposto {} e adjacente {}, valor da hipotenusa será {:.2f}.'.format(co, ca, math.hypot(ca, co)))
