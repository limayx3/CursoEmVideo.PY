#ler 7 valores numéricos e cadasrtá-los numa lista composta única, mas que mantenha separados os pares dos ímpares.
#No fim mostrar pares e ímpares em ordem crescente

valores = [[], []]
num = 0

for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)

print(f'Os pares em ordem crescente são: {sorted(valores[0])}')
print(f'Já os ímpares ficam: {sorted(valores[1])}')
