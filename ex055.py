#LER PESO DE 5 PESSOAS, MOSTRAR QUAL MAIOR E QUAL MENOR
lista = []
for c in range(0, 5):
    peso = float(input('Informe um peso em kg: '))
    lista.append(peso)
print('O maior valor é {}kg.'.format(max(lista)))
print('Já o menor valor é {}kg.'.format(min(lista)))
