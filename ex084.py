#LER NOME E PESO DE VÁRIAS PESSOAS E ARMAZENAR EM LISTA. MOSTRAR NO FIM:
#A - Quantos foram cadastrados
#B - Uma lista com os mais pesados
#C - Uma lista com as mais leves

cadastros = []
pessoa = []
cont = pesomax = pesomin = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if pessoa[1] > pesomax:
        pesomax = pessoa[1]
    if cont == 0 or pessoa[1] < pesomin:
        pesomin = pessoa[1]
    cadastros.append(pessoa[:])
    pessoa.clear()
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break

print(f'Após cadastrarmos {cont} pessoa(s), vimos que:')                       #A

print(f'O maior dos pesos é {pesomax}kg, da(s) pessoa(s): ', end='')            #B
for c in range(0, len(cadastros)):
    if cadastros[c][1] == pesomax:
        print(f'{cadastros[c][0]}', end='... ')

print(f'\nJá o menor peso observado, de {pesomin}kg, pertence à: ', end='')    #C
for c in range(0, len(cadastros)):
    if cadastros[c][1] == pesomin:
        print(f'{cadastros[c][0]}', end='... ')
