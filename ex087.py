#Aprimorando o ex086, mostrar também:
#A - A soma de todos os valores pares digitados;
#B - A soma dos valores da terceira coluna
#C - O maior valor da segunda linha

matriz = [[], [], []]
num = somapar = soma3a = maior = 0

for c in range (0, 3):
    for n in range (0, 3):
        num = int(input('Digite o valor: '))
        matriz[c].append(num)

#A
for c in range (0, 3):
    for n in range(0, 3):
        if matriz[c][n] % 2 == 0:
            somapar += matriz[c][n]
print(f'A soma dos pares deu: {somapar}.')

#B
for c in range(0, 3):
    soma3a += matriz[c][2]
print(f'A soma dos valores da 3ª coluna deu: {soma3a}.')

#C
for c in range (0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da 2ª linha é: {maior}.')
