#ESCREVA UM PROGRAMA UE CONVERTA UMA TEMPERATURA DIGITADA EM °C E CONVERTA PARA °F
"""
1. Ler temperatura em celsius
2. Calcular temperatura em farenheit
3. Exibir temperatura em farenheit
"""

c = float(input('Digite a temperatura em graus Celsius:'))
f = (c * 9) / 5 + 32
print('{}°C equivalem à {}°F.'.format(c, f))
