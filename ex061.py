#DESAFIO EX051, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO O WHILE.

t1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
escolha = 0
c = 1
termo = t1

while c <= 10:
    print('{} → '.format(termo), end='')
    termo += r
    c += 1

print('Fim do programa.')