#LER NÚMERO INTEIRO E INFORMAR SE É PRIMO (DIVISÍVEL POR 1 E POR ELE MESMO)

n = int(input('Digite um número: '))
primo = 0

for c in range(1, n+1):
    if n % c == 0:
        print('\033[35m{}\033[m'.format(c), end=' ')
        primo += c
    else:
        print('\033[36m{}\033[m'.format(c), end=' ')
if primo == 1 + n: #podemos criar uma variável contadora que adiciona 1 toda vez que ele for divisível, então se for só 2x é primo, mas se for mais não é
    print('\nÉ um número PRIMO!')
else:
    print('\nNão é um número primo!')
    