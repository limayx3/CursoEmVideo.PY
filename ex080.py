#DIGITAR 5 VALORES NUMÉRICOS E CADASTRÁ-LOS NUMA LISTA JÁ EM ORDEM CRESCENTE (SEM USAR 'SORT()')
#A CADA ADIÇÃO INFORMAR EM QUAL POSIÇÃO FOI ADICIONADO. MOSTRAR LISTA NA TELA.

valores = []
novonum = 0

for c in range(0, 5):
    novonum = int(input('Digite um número: '))
    if c == 0 or novonum > valores[-1]:             #se for o 1º valor (índice c será 0) ou novo número for maior que o último valor da lista (-1)
        valores.append(novonum)                     #então append esse novonum na lista.
        print(f'{novonum} adicionado no fim da lista!')
    else:
        pos = 0                                     #utilizamos uma nova variável para varrer as posições da lista, iniciando pelo índice 0
        while pos < len(valores):                   #enquanto a posição for menor que o tamanho da lista valores
            if novonum <= valores[pos]:             #se o novo número for <= ao número na lista valores [índice conforme posição]
                valores.insert(pos, novonum)        #inserir esse novo número na posição pos
                print(f'{novonum} adicionado na posição {pos} da lista.')
                break                               #ao ser inserido número, não precisamos verificar novamente a posição dele, portanto break
            pos =+1                                 #caso não seja inserido, a posição precisa ser 1 casa maior para que ande na régua de índices

print(f'Os valores digitados, em ordem crescente, foram: {valores}.\n')