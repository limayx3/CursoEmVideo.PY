#PERMITIR DIGITAR N VALORES, PARANDO APENAS QUANDO O USER DIGITAR 999, ENTÃO MOSTRAR A SOMA DE TODOS QUE FORAM DIGITADOS (EXCETO ESSE 999, QUE É O FLAG)
c = soma = valor = 0

'''while valor != 999:
    valor = int(input('Digite um valor a ser somado [999 para parar]: '))
    c += 1
    soma += valor
print('Foram digitados {} valores e sua soma é {}.'.format(c-1, soma-999))'''

valor = int(input('Digite um valor [999 para parar]: '))
while valor != 999:
    soma += valor
    c += 1
    valor = int(input('Digite um valor [999 par parar]: '))

print('Você digitou {} números e a soma deles é {}.'.format(c, soma))