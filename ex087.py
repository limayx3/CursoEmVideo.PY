#Aprimorando o ex086, mostrar também:
#A - A soma de todos os valores pares digitados;
#B - A soma dos valores da terceira coluna
#C - O maior valor da segunda linha

matriz = [[], [], []]
num = somapar = soma3a = maior = 0

for c in range (0, 3):
    for n in range (0, 3):
        num = int(input(f'Digite o valor para a posição [{c}, {n}]: '))
        matriz[c].append(num)
print('='*45)
for c in range(0, 3):
    for n in range(0, 3):
        print(f'[{matriz[c][n]:^5}]', end=' ')
    print()
print('='*45)

print('A: ', end='')      #A
for c in range (0, 3):
    for n in range(0, 3):
        if matriz[c][n] % 2 == 0:
            somapar += matriz[c][n]
print(f'A soma dos pares deu: {somapar}.')

print('B: ', end='')      #B
for c in range(0, 3):
    soma3a += matriz[c][2]
print(f'A soma dos valores da 3ª coluna deu: {soma3a}.')

print('C: ', end='')      #C
for c in range (0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da 2ª linha é: {maior}.')
print('='*45)
