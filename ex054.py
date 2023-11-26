#LER ANO DE NASCIMENTO DE 7 PESSOAS E MOSTRAR QUANTAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES (21 ANOS)
from datetime import date
hoje = date.today().year
ma = 0
me = 0
for c in range(0, 7): #ou (1, 8)
    nasc = int(input('Informe seu ano de nascimento: '))
    idade = hoje - nasc
    if idade >= 21:
        ma += 1
    else:
        me += 1
print('\033[1,35m{} já são maiores\033[m, mas \033[1,36m{} ainda não\033[m.'.format(ma, me))
