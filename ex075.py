#LER 4 VALORES PELO TECLADO E ADICIONÁ-LOS À TUPLA, ENTÃO MOSTRAR:
#A - QUANTAS VEZES APARECEU O ALGARISMO 9;
#B - EM QUE POSIÇÃO ESTÁ O PRIMEIRO NÚMERO 3; E
#C - QUAIS SÃO PARES

valores = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')))
print(f'Foram digitados os números: {valores}.')

print(f'A) O algarismo 9 foi digitado {valores.count(9)} vezes;')
if 3 in valores:
    print(f'B) O primeiro algarismo 3 está na {valores.index(3)+1}ª posição.')
else:
    print('B) O algarismo 3 não foi digitado em nenhum momento.')

print(f'C) Os números pares digitados foram:', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
