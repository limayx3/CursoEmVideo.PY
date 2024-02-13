'''CRIAR UMA TUPLA COM VÁRIAS PALAVRAS
(SEM ACENTUAÇÃO) E MOSTRAR AS VOGAIS DE
CADA PALAVRA.'''

palavras = ('celular', 'impressora', 'monitor',
            'mouse', 'caderno', 'notebook',
            'canetas', 'estojo',
            'ar condicionado')

for p in palavras:
    print(f'\nEm {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
