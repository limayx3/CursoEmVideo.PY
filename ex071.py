#SIMULAR CAIXA ELETRÔNICO PERGUNTANDO VALOR À SACAR E INFORMANDO QUANTAS CÉDULAS DE CADA VALOR (R$50, 20, 10 E 1) SERÃO ENTREGUES.

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

print('\nObrigado, volte sempre.\n')
