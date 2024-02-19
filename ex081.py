#LER VÁRIOS NÚMEROS E COLOCAR NUMA LISTA, QUESTIONANDO SE QUER CONTINUAR. MOSTRAR:
#A - QUANTOS NÚMEROS FORAM DIGITADOS;
#B - A LISTA DE VALORES ORDENADA DE FORMA DECRESCENTE;
#C - SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA.

valores = []
c = 0

while True:
    valores.append(int(input('Digite um valor: ')))
    c += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SsNn':
        print('Valor não pode ser aceito. \nDigite S para sim e N para não.')
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break


print(f'Na lista foram digitados os seguintes valores: {valores}')
print(f'{" ONDE:":=>61}')
print(f'A - Foram digitados {c} números;')
valores.sort(reverse=True)
print(f'B - Lista em ordem decrescente é: {valores}')
print('C - Temos o 5 na lista? ', end='')
if 5 in valores:
    (print(f'Sim, temos {valores.count(5)}x o número 5 nessa lista.'))
else:
    print('Não, este número não foi digitado.')
print('=' * 61)
