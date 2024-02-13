#DIGITAR VÁRIOS VALORES NUMÉRICOS, CADASTRANDO-OS NUMA LISTA, MAS CASO REPETIDO NÃO ADICIONAR.
#INFORMAR SE FOI ADICIONADO E QUESTIONAR SE QUER CONTINUAR.
#MOSTRAR TODOS OS VALORES ÚNICOS EM ORDEM CRESCENTE.

valores = []
novonum = 0
continuar = ''

while True:
    novonum = (int(input('Digite um valor: ')))
    if novonum not in valores:
        valores.append(novonum)
        print(f'O valor {novonum} foi adicionado com sucesso.')
    else:
        print(f'Você digitou o valor {novonum} repetido e não adicionamos.')

    continuar = str(input('Deseja continuar? [s/n] '))
    if continuar.lower().strip()[0] == 'n':
        break
    while continuar.lower().strip()[0] != 's':
        continuar = str(input('Este valor não pode ser aceito. Deseja continuar? [s/n] '))

print(f'Foram digitados os valores: ', end='')
for p, v in enumerate (valores):
    print(f'{v}', end=' ')
