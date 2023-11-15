#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
#(1) BINÁRIO, (2) OCTAL E (3) HEXADECIMAL (BASE NUMÉRICA) ENTÃO MOSTRAR VALOR CONVERTIDO CONFORME ESCOLHA

num = int(input('Informe um número inteiro: '))
print('Para qual base deseja realizar a conversão? 1 (Binário), 2 (Octal) ou 3 (Hexadecimal)?')
conversão = int(input('Digite apenas o número da opção desejada: '))

if conversão == 1:
    print('O número {} convertido para BINÁRIO é: {}.'.format(num, bin(num)[2:]))
elif conversão == 2:
    print('O número {} convertido para OCTAL é: {}.'.format(num, oct(num)[2:]))
elif conversão == 3:
    print('O número {} convertido para HEXADECIMAL é: {}.'.format(num, hex(num)[2:]))
else:
    print('Você precisa escolher uma das 3 opções oferecidas.')

print('Tenha um excelente dia.')