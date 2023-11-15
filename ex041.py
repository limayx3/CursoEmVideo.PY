#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
#ATÉ 9 ANOS - MIRIM
#DE 10 À 14 ANOS - JUVENIL (INFANTIL)
#DE 15 À 19 - JUNIOR
#20 ANOS - SÊNIOR
#21 OU ACIMA - MASTER
"""
1. Importar biblioteca datetime e usar função date
2. Ler ano de nascimento de um atleta
3. Comparar nascimento com ano atual e calcular idade
4.1. Se idade <=9: Mirim
4.2. Se idade >=10 and <=14: Juvenil
4.3. Se idade >=15 and <=19: Júnior
4.4. Se idade == 20: Sênior
4.5. Se idade >=21> Master
"""
import datetime

nasc = int(input('\nInforme o ano de seu nascimento: '))
ano = datetime.date.today().year
idade = ano - nasc

#É POSSÍVEL COLOCAR DO 1º ELIF EM DIANTE APENAS A PARTE MAIOR (EX: IDADE < 15, NO OUTRO IDADE < 20...)
if idade < 10:
    print('Este nadador completa {} anos esse ano e competirá na categoria MIRIM.'.format(idade))
elif idade >= 10 and idade < 15:
    print('Este nadador completa {} anos esse ano e competirá na categoria JUVENIL/ INFANTIL.'.format(idade))
elif idade >= 15 and idade < 20:
    print('Este nadador completa {} anos esse ano e competirá na categoria JÚNIOR.'.format(idade))
elif idade >= 20 and idade < 26:
    print('Este nadador completa {} anos esse ano e competirá na categoria SÊNIOR.'.format(idade))
else:
    print('Este nadador completa {} anos esse ano e competirá na categoria MASTER.'.format(idade))

print('\n\033[4;36;47mIndependente da categoria, se dedique, treine bastante e boa sorte!\033[m\n')
