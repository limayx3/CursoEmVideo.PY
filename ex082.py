#LER VÁRIOS NÚMEROS E COLOCAR NUMA LISTA, QUESTIONANDO SE QUER CONTINUAR.
#DEPOIS CRIAR 2 LISTAS EXTRAS CONTENDO OS PARES E OS ÍMPARES DIGITADOS.
#MOSTRAR AS 3 LISTAS.
valores = []
par = []
ímpar = []
continuar = ''

while True:
    valores.append(int(input('Informe um valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Valor digitado não aceito.\nDeseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break

for num in valores:
    if num % 2 == 0:
        par.append(num)
    else:
        ímpar.append(num)
print('=' * 35)
print(f'Nossa lista: {valores} \nOs pares: {par} \nOs ímpares: {ímpar}')
print('=' * 35)
