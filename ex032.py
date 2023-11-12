#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO
from datetime import date
ano = int(input('Informe o ano para a verificação, sendo 0 o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print('{} foi ou será um ano BISSEXTO!'.format(ano))
else:
    print('{} foi ou será um ano com 365 dias!'.format(ano)) 
