#LER NÚMEROS ENTRE 0 E 20 PELO TECLADO E IDENTIFICAR NUMA TUPLA O VALOR POR EXTENSO. NÃO ACEITAR VALORES FORA DO RANGE

numerais = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
numext = ('zero' , 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

#VERIFICAR SE PRECISA TER LOOP PRA VER QUANTOS NÚMEROS QUISER

escolha = ' '
while escolha not in numerais:
    escolha = int(input('Informe um número entre 0 e 20: '))

print(f'Você digitou {escolha} que por extenso é {numext[escolha]}.')
