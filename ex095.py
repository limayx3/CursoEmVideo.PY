#Gerenciador de aproveitamento de jogador que lê o nome, quantas partidas jogadas e quantos gols feitos por partida.
#Tudo guardado num dicionário, incluindo o total de gols feitos no campeonato
#Aprimorar ex093, para funcionar com vários jogadores, incluindo exibir lista com códigos pra cada um e visualização de detalhe individual por código.

time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: ')).title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Gols na {c+1}ª partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        continuar = str(input('Deseja cadastrar outro jogador? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Informação inválida. Digite S para SIM e N para NÃO.')
    if continuar == 'N':
        break

print('~*~ ' * 15)
print('Cód. ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:^4} ', end='')
    for d in v.values():
        print(f'{str(d):20}', end='')
    print()
print('~*~ ' * 15)

while True:
    busca = int(input('Mostrar dados do jogador com código: [999 p/ parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não temos um jogador com o código {busca}!!! Cê tem burro é?')
    else:
        print('_' * 40)
        print(f'→ Dados do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'       JOGO {i+1} → {g} gols;')
        print('-' * 40)
print('~*~ FIM DO PROGRAMA ~*~\n')
