#Crie um programa que cria uma matriz de dimensão 3x3 (igual jogo da velha), preenchendo com valores do teclado.
#No fim mostrá-la com a formatação correta

matriz = [[], [], []]
num = 0

for c in range (0, 3):
    for n in range(0, 3):
        num = int(input('Informe o valor: '))
        matriz[c].append(num)

for c in range(0, 3):
    for n in range (0, 3):
        print(f'[ {matriz[c][n]} ]', end=' ')

