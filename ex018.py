#FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO E MOSTRE SEU SENO, COSSENO E TANGENTE DELE.
#EXISTE MÓDULO QUE FACILITA
"""
1. Ler ângulo
2. Exibir seno
3. Exibir cosseno
4. Exibir tangente
"""

import math
angle = int(input('Informe o ângulo (apenas números): '))
s = math.sin(angle)
c = math.cos(angle)
t = math.tan(angle)
print('\nPara o ângulo {}, o seno é {:.2f} radianos.'.format(angle, s))
print('Para o ângulo {}, o cosseno é {:.2f} radianos.'.format(angle, c))
print('Para o ângulo {}, a tangente é {:.2f} radianos.\n'.format(angle, t))
