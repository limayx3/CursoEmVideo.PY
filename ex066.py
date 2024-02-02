#LER VÁRIOS NÚMEROS INTEIROS, PARANDO QUANDO O 999 (FLAG) FOR DIGITADO.
#MOSTRAR QUANTOS NÚMEROS FORAM DIGITADOS E SUA SOMA DESCONSIDERANDO O FLAG.

c = s = 0

while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n

print(f'Você digitou {c} números e o somatório deles é {s}.')
