#LER NOME E PREÇO DE VÁRIOS PRODUTOS, QUESTIONANDO SE USER QUER CONTINUAR A CADA FIM DE CADASTRO.
#AO FINDAR, MOSTRAR: (1) TOTAL GASTO NA COMPRA, (2) QUANTOS PRODUTOS CUSTAM MAIS DE R$1000 E (3) QUAL PRODUTO MAIS BARATO.

total = preço2 = milhar = continuar = 0
preço1 = 9999999999999999
produto = barato = ''

while continuar == 0:
    continuar = int(input('Deseja cadastrar um produto?\n0 para sim\nSua resposta: '))
    if continuar != 0:
        break
    produto = str(input('PRODUTO: '))
    preço2 = float(input('PREÇO: R$ '))
    total += preço2
    if preço2 > 1000:
        milhar += 1
    if preço2 < preço1:
        preço1 = preço2
        barato = produto
    

print(f'\n###COMPRA FINALIZADA###\n→TOTAL: R$ {total:.2f}\n→Produtos com preço maior que R$ 1000.00: {milhar} produtos.\n→Produto mais barato: {barato} à R$ {preço1}.')
print('#' * 23, '\n')
