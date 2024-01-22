#LER 2 VALORES E MOSTRAR MENU NA TELA COM:
#(1) SOMA, (2) MULTIPLICAÇÃO, (3) MAIOR, (4) NOVOS NÚMEROS E (5) SAIR DO PROGRAMA
#ELE DEVERÁ REALISAR A OPÇÃO ESCOLHIDA E DAR A RESPOSTA

n1 = int(input('Informe o primeiro valor inteiro: '))
n2 = int(input('Informe o segundo valor inteiro: '))

escolha = 0
while escolha != 5:
    print('As possíveis opções são:')
    print('''      [ 1 ] soma
      [ 2 ] multiplicação
      [ 3 ] ver o maior deles
      [ 4 ] digitar novos números
      [ 5 ] sair do programa''')
    escolha = int(input('Digite o algarismo correspondente a sua opção: '))
    if escolha == 1:
        soma = n1 + n2
        print('Soma = {}'.format(soma))
    elif escolha == 2:
        multiplicação = n1 * n2
        print('Multiplicação = {}'.format(multiplicação))
    elif escolha == 3:
        lista = [n1, n2]
        print('Maior deles = {}'.format(max(lista)))
    elif escolha == 4:
        n1 = int(input('Informe outro 1º valor: '))
        n2 = int(input('Informe outro 2º valor: '))

print('Fim do nosso programa. Obrigada.')
