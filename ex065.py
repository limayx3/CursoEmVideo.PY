#LER VÁRIOS NÚMEROS INTEIROS E NO FIM DA EXECUÇÃO MOSTRR MÉDIA, MENOR E MAIOR VALOR. QUESTIONAR SEMPRE AO USER SE QUER DIGITAR MAIS.

soma = c = média = menor = maior = 0
escolha = 's'

while escolha in 's':
    valor = int(input('Digite um valor: '))
    soma += valor
    c += 1
    if c == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    escolha = str(input('Quer digitar mais um valor? s/n ')).strip().lower()[0]
    
média = soma / c
print('Você digitou {} números e sua média é {}.'.format(c, média))
print('A soma dos valores digitados é {}.'.format(soma))
print('O maior e o menor valor foram, respectivamente: {} e {}.'.format(maior, menor))
