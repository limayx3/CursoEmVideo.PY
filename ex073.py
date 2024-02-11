#PREENCHER TUPLA COM OS 20 PRIMEIROS DO BRASILEIRÃO, NA ORDEM DE COLOCAÇÃO. MOSTRAR:
#A - APENAS OS 5 PRIMEIROS;
#B - OS ÚLTIMOS 4 COLOCADOS;
#C - TODOS EM ORDEM ALFABÉTICA; E
#D - POSIÇÃO DO CHAPECOENSE/ FLAMENGO;

brasileirão = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
count = 1

print(f'Os 5 primeiros são, em ordem de colocação: \n→{brasileirão[0:5]}')
print(f'A zona de rebeixamento é formada por: \n→{brasileirão[20:15:-1]}')
print(f'Em ordem alfabética: \n→{sorted(brasileirão)}')

