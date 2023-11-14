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