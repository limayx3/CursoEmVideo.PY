#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILÍMETROS:
"""
1. Ler valor em metros
2. Converter de metros para centímetros
3. Converter de metros para mílímetros
4. Exibir valor em metros, centímetros e milímetros
"""

valor = float(input('Digite o valor em metros: '))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print('{}m equivale à: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(valor, km, hm, dam, dm, cm, mm))
