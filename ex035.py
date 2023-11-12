#LER O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO
#EXISTE UM PRINCÍPIO MATEMÁTICO PARA FORMAR TRIÂNGULOS!!!
"""
1. Ler comprimento das 3 retas
2. calcular se formariam um triângulo
3. Mostrar se formariam um triângulo
"""
r1 = float(input('Informe o valor da reta 1 em metros: '))
r2 = float(input('Informe o valor da reta 2 em metros: '))
r3 = float(input('Informe o valor da reta 3 em metros: '))
print('Para os valores informados por você, respectivamente {}, {} e {},...'.format(r1, r2, r3))

if (r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2):
    print('\n... Temos sim a formação de um triângulo!')
else:
    print('\n... Infelizmente não temos um triângulo.')
