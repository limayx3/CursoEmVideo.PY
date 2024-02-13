#LER 5 VALORES NUMÉRICOS E GUARDAR NUMA LISTA. NO FIM MOSTRAR MAIOR, MENOR E AS POSIÇÕES DOS MESMOS
#MOSTRAR TODAS AS POSIÇÕES DOS VALORES

valores = []
for c in range(0,5):
    valores.append(int(input(f'Informe o {c+1}º valor: ')))

print('=' * 25)
print('Você digitou os valores:')
for pos, número in enumerate(valores):
    print(f'Índice {pos} → {número}')  
print('=' * 25)


print(f'O maior destes valores é o {max(valores)}, que está(ão) no(s) índice(s) ', end='')
for c in range (0, len(valores)):
    if valores[c] == max(valores):
        print(f'{c}', end=' ')

print(f'\nO menor desses valores é o {min(valores)}, que está(ão) no(s) índice(s) ', end='')
for c in range (0, len(valores)):
    if valores[c] == min(valores):
        print(f'{c}', end=' ')
