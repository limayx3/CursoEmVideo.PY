#Gerenciador de aproveitamento de jogador que lê o nome, quantas partidas jogadas e quantos gols feitos por partida.
#Tudo guardado num dicionário, incluindo o total de gols feitos no campeonato
#"O jogador fulano jogou X partidas, onde: Na 1ª fez x gols, na segunda x gols... Num total de x gols."

jogador = {}
gols = []
soma = gol = média = 0

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Jogou quantas partidas? '))
for p in range(0, jogador['partidas']):
    gol = int(input(f'Quantos gols feitos na {p+1}º partida? '))
    soma += gol
    gols.append(gol)
jogador['gols'] = gols[:]
jogador['totgols'] = soma
média = soma / jogador['partidas']

print('='*30)
print(f'O jogador {jogador['nome']} jogou {jogador['partidas']} jogos neste campeonato, onde:')
for c in range(0, jogador['partidas']):
    print(f'Na {c+1}ª partida, marcou {jogador['gols'][c]} gol(s).')
if média >= 2.5:
    print(f'Este jogador totalizou {soma} gol(s), com média de {média} gol(s) por partida. Estrela!')
elif média <= 0.5:
    print(f'Tá na hora de repensar o treinamento ou substituí-lo, decepcionante ter {soma} gol(s) e média {média} por partida.')
else:
    print(f'Com total de {soma} gol(s) e média de {média} gol(s) por partida, temos um bom desempenho!')
    