#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO"

cidade = str(input('Informe o nome da cidade: ')).strip()
print('SANTO' in cidade[0:5].upper())
