#Criar a função escreva() que recebe um texto qualquer como parâmetro e mostre-o com linhas superior e inferior de til (~), adaptadas ao tamanho do texto

def escreva(txt):
    tamanho = len(txt) + 4
    print('~'*tamanho)
    print(f'  {txt:^}')
    print('~'*tamanho)


frase = str(input('Informe a frase à imprimir: '))
escreva(frase)
