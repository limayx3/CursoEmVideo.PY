#SIMULAR CAIXA ELETRÔNICO PERGUNTANDO VALOR À SACAR E INFORMANDO QUANTAS CÉDULAS DE CADA VALOR (R$50, 20, 10 E 1) SERÃO ENTREGUES.

'''MINHA SOLUÇÃO:
saque = nota50 = nota20 = nota10 = nota1 = opção = 0

print('~*~ Banco da Nathy ~*~')
print('Digite:\n 1 - SAQUE\n 2 - EXTRATO(fake)\n 3 - EMPRÉSTIMO(fake)')
opção = int(input('Sua opção: '))
while opção == 1:
    print('Você escolheu SAQUE de valor.\n')
    saque = float(input('Valor do saque:\nR$ '))
    nota50 = int(saque / 50)
    nota20 = int((saque % 50) / 20)
    nota10 = int(((saque % 50) % 20) / 10)
    nota1 = int((((saque % 50) % 20) % 10) / 1)
    print('=$' * 20)
    print(f'Você vai sacar:\n[{nota50:^5}] cédula(s) de R$ 50,00\n[{nota20:^5}] cédula(s) de R$ 20,00\n[{nota10:^5}] cédula(s) de R$ 10,00\n[{nota1:^5}] cédula(s) de R$  1,00')
    print('=$' * 20)
    opção = int(input('Deseja sacar novamente? 1 para sim: '))

print('\nObrigado, volte sempre.\n')'''

#SOLUÇÃO DO GUANABARA:

valor = int(input('Valor á ser sacado:\nR$ '))
total = valor
cédula = 50
total_céd = 0

while True:
    if total >= cédula:     #se o total atual for maior ou igual ao valor da cédula
        total -= cédula     #tentar tirar esse valor do total e
        total_céd += 1      #adicionar 1 na quantidade dessa cédula
    else:
        if total_céd > 0:   #Apenas imprimir se o total de cédulas for maior que 0
            print(f'Cédulas de {cédula:>2} reais: {total_céd}.')
        if cédula == 50:    #se a cédula atual for  valor 50 e não conseguimos mais tirar esse valor
            cédula = 20     #vira uma cédula de 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_céd = 0
        if total == 0:
            break

print('Volte sempre.')