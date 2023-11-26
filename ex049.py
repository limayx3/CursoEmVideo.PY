#REFAZER EX009 DA TABUADA QUE O USUÁRIO ESCOLHE, MAS COM LAÇO FOR

n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:>2} = {:<5}'.format(n, c, n*c))
