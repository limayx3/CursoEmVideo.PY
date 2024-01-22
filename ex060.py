#LER NÚMERO QUALQUER E MOSTRAR SEU FATORIAL

#Minha resolução
fatorial = int(input('Vamos calcular o fatorial de: '))
c = 1
resultado = 1

while c <= fatorial:
    resultado *= c
    c += 1

print('O fatorial de {} é igual à {}.'.format(fatorial, resultado))

'''Utilizando o FOR:

for c in range(1, fatorial+1)
    resultado *= c

print('O fatorial de {} é {}.'.format(fatorial, resultado))'''


'''RESOLUÇÃO DO GUANABARA:

from math impot factorial
n = int(input('Digite um número para o cálculo do fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''