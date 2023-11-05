#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILÍMETROS:
"""
1. Ler valor em metros
2. Converter de metros para centímetros
3. Converter de metros para mílímetros
4. Exibir valor em metros, centímetros e milímetros
"""

valor = float(input('Digite o valor em metros: '))
cm = valor * 100
mm = valor * 1000
print('R: {} metros equivale à {} centímetros e {} milímetros.'.format(valor, cm, mm))
