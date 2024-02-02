#LER NOME E PREÇO DE VÁRIOS PRODUTOS, QUESTIONANDO SE USER QUER CONTINUAR A CADA FIM DE CADASTRO.
#AO FINDAR, MOSTRAR: (1) TOTAL GASTO NA COMPRA, (2) QUANTOS PRODUTOS CUSTAM MAIS DE R$1000 E (3) QUAL PRODUTO MAIS BARATO.

total = cont = milhar = menor = 0
barato = ''

while True:
    produto = str(input('PRODUTO: '))
    preço = float(input('PREÇO: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        milhar += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    #Dessa forma enquanto a resposta não estiver dentro de 'SN' o programa vai questionar a mesma coisa (18, 19 e 20)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja cadastrar outro produto? [S/N]\nSua resposta: ')).strip().upper()[0]
    if resposta == 'N':
        break

print('\n###COMPRA FINALIZADA###')
print(f'→TOTAL: R$ {total:.2f}\n→Produtos com preço maior que R$ 1000.00: {milhar} produtos.\n→Produto mais barato: {barato} à R$ {menor}.')
print('#' * 23, '\n')
