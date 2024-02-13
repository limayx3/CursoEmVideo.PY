'''CRIAR UMA TUPLA ÚNICA COM NOMES DE
PRODUTOS E SEUS PREÇOS (EM SEQUÊNCIA).
MOSTRAR NO FIM UMA SAÍDA TABULADA COM
ESSA LISTA'''

lista = ('Quatro queijos', 5.25,
         'Milho', 4.5,
         'Frango com catupiry', 4.25,
         'Palmito', 5,
         'Chocolate meio-a-meio', 4.5,
         'Nutella', 5.5)

print('=' * 40)
print(f'{"CARDÁPIO":^40}')
print('=' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>6.2f}')
