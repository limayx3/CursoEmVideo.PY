#REFAZER EX061 QUESTIONANDO SE QUER MOSTRAR MAIS TERMOS, ONDE SE DIGITAR "0" ELE PARA A BRINCADEIRA

''' MINHA RESOLUÇÃO:
t1 = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = t1
c = 1
escolha = 999'''

'''    while escolha != 0:
        print(''''''As possíveis opções serão:
            1 - Ver os 10 primeiros termos dessa PA
            2 - Ver mais 10 termos da PA
            0 - Sair do programa'''''')
        escolha = int(input('Escolha uma das opções, por obséquio: '))
        if escolha == 1:
            print('Os primeiros 10 termos dessa PA são:')
            while c <= 10:
                print('{}º = {}.'.format(c, termo))
                termo += r
                c += 1
        if escolha == 2:
            mais = c + 9
            while c <= mais:
                print('{}º = {}.'.format(c, termo))
                termo += r
                c += 1
    print('Fim do programinha.')'''

#RESOLUÇÃO DO GUANABARA:
print('Vamos construir Progressões Aritméticas?')
print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
t1 = int(input('- 1º termo da PA: '))
r = int(input('- razão da PA: '))
termo = t1
c = 1
total = 0 #quantos termos vai mostrar no total
adicionar = 10 #quntos termos quer adicionar

while adicionar != 0:
    total += adicionar
    while c <= total:
        print('{} → '.format(termo), end='')
        termo += r
        c += 1
    adicionar = int(input('Quantos termos mais vossa excelência deseja visuvializar? '))
print('Nossa progressão teve {} termos. SUPIMPA!'.format(total))
