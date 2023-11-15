#ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
#À VISTA NO DINHEIRO/ PIX - 10% DE DESCONTO
#À VISTA NO CARTÃO - 5% DE DESCONTO
#EM ATÉ 2X NO CARTAO - PREÇO NORMAL (INFORMAR VALOR DAS PARCELAS)
#3X OU MAIS NO CARTÃO - 20% DE JUROS (INFORMAR VALOR DAS PARCELAS)
"""
1. Ler valor do produto
2. Informar quais condições de pagamento existem
3. Ler condição de pagamento desejada
3.1. Se condição escolhida for à vista no dinheiro/pix: preço = valor - (valor * 0.1)
3.2. Se condição escolhida for à vista no cartão: preço = valor - (valor * 0.05)
3.3. Se condição escolhida for 2x no cartão: preço = valor
3.4. Se condição escolhida for 3x ou mais no cartão: preço = valor * 1.2
"""

valor = float(input('Qual o valor normal do produto? R$'))
print('''As formas de pagamento disponíveis são:
      1 - À vista no dinheiro/ cheque/ pix
      2 - À vista no cartão, seja débito ou crédito
      3 - Até 2x no cartão de crédito
      4 - 3x ou mais no cartão de crédito''')
opção = int(input('Digite a opção escolhida: '))
print('Você escolheu {}.'.format(opção))

if opção == 1:
    preço = valor - (valor * 0.1)
    print('Na opção à vista no dinheiro/ cheque/ pix, você recebe um desconto e pagará R${:.2f}.'.format(preço))
elif opção == 2:
    preço = valor - (valor * 0.05)
    print('Na opção à vista no cartão, seja débito ou crédito, você recebe um desconto e pagará R${:.2f}.'.format(preço))
elif opção == 3:
    print('Na opção até 2x no cartão de crédito você pagará o preço normal, ou seja, R${:.2f}.'.format(valor))
    print('As parcelas serão de R${:.2f}.'.format(valor / 2))
elif opção == 4:
    preço = valor * 1.2
    print('Na opção 3x ou mais no cartão de crédito você terá um acréscimo no valor, pagando no total R${:.2f}.'.format(preço))
    parcelas = int(input('Em quantas vezes vai querer dividir? Pode ser até 12x. '))
    print('Ao escolher pagar em {}x, as parcelas terão o valor de R${:.2f}.'.format(parcelas, preço / parcelas))
else:
    print('Você digitou uma opção inválida, tente novamente.')
print('Obrigada por negociar conosco!')
