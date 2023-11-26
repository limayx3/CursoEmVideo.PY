#LER FRASE E INFORMAR SE É PALÍNDROMO (ler de trás pra frente é a mesma coisa), DESCONSIDERANDO OS ESPAÇOS. EX: O LOBO AMA O BOLO; A SACADA DA CASA.
#DIGITAR FRASE SEM ACENTOS, MAS COM ESPAÇOS (QUE O PROGRAMA VAI DESCONSIDERAR SOZINHO)

frase = str(input('Digite uma frase: ')) #podemos colocar coladinho aqui .upper().strip()
frase = frase.upper()
frase = frase.strip()
dividida = frase.split()
concatenada = ''.join(dividida)
iconcatenada = concatenada[::-1]
if concatenada == iconcatenada:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
