#ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. DEVE PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELA NAO PODE EXCEDER 30% DO SALÁRIO, OU O EMPRÉSTIMO SERÁ NEGADO.
"""
1. Ler valor total da casa
2. Ler valor bruto do salário mensal
3. Ler em quantos meses o usuário quer pagar
4. Calcular valor da prestação mensal
5. Se prestação >= 30% do salário = negado (indicar possibilidade de pagar em mais meses)
6. Se prestação < 30% do salário = aprovado
"""
color = {'clean': '\033[m', 'aware':'\033[1;31;43m', 'positive':'\033[1;32;40m', 'cute':'\033[1;35;46m', 'black':'\033[7;30;47m'}
comprador = str(input('Qual é seu nome? ')).strip()
casa = float(input('Informe o valor da casa à ser comprada: R$'))
salário = float(input('{}{}{}, qual é o valor bruto de seu salário mensal? R$'.format(color['cute'], comprador, color['clean'])))
período = int(input('Em quantos meses gostaria de quitar essa dívida? '))

prestação = casa / período
percentil = salário * 0.3

if prestação >= percentil:
    print('Infelizmente o valor das parcelas é {}R${:.2f}{} e ultrapassa o percentual limite de seu salário. Empréstimo {}NEGADO{}.'.format(color['aware'], prestação, color['clean'], color['aware'], color['clean']))
    print('{}Considere aumentar a quantidade de meses para a quitação do financiamento e tente novamente.{}'.format(color['black'], color['clean']))
else:
    print('Seu empréstimo está {}APROVADO{}! Você pagará prestações de {}R${:.2f}{}, por {}{:.1f} anos{}.'.format(color['positive'], color['clean'], color['positive'], prestação, color['clean'], color['cute'], (período / 12), color['clean']))
print('Obrigada pelo seu interesse, {}{}{}!!!'.format(color['cute'], comprador, color['clean']))
