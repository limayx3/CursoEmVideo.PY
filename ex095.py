#Gerenciador de aproveitamento de jogador que lê o nome, quantas partidas jogadas e quantos gols feitos por partida.
#Tudo guardado num dicionário, incluindo o total de gols feitos no campeonato
#Aprimorar ex093, para funcionar com vários jogadores, incluindo exibir lista com códigos pra cada um e visualização de detalhe individual por código.

jogadores = []
jogador = {}
gols = []
média = soma = gol = 0

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input('Partidas jogadas: '))
    for p in range(0, jogador['partidas']):
        gol = int(input(f'Total de gols da {p+1}ª partida: '))
        soma += gol
        gols.append(gol)
    jogador['gols'] = gols[:]
    jogador['totgols'] = soma
    média = soma / jogador['partidas']
    jogadores = jogador.copy()
    jogador.clear()

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f'{"Cód":<5}|{"Nome do Jogador":^30}')
for j in range(0, len(jogadores)):
    print(f'{j:<5}|{jogadores[j]['nome']:^30}')


