#DIGITAR 5 VALORES NUMÉRICOS E CADASTRÁ-LOS NUMA LISTA JÁ EM ORDEM CRESCENTE (SEM USAR 'SORT()')
#A CADA ADIÇÃO INFORMAR EM QUAL POSIÇÃO FOI ADICIONADO. MOSTRAR LISTA NA TELA.

valores = []
novonum = 0


valores.append(int(input('Digite um número: ')))
for c in range(0, 4):
    novonum = int(input('Digite um número: '))
    if novonum >= max(valores):
        valores.insert(c+1, novonum)
    elif novonum < min(valores):
        valores.insert(c-1, novonum)


print(valores)