#FAÇA UM PROGRAMA QUE LEIA 3 NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL O MENOR.
print('Vamos comparar 3 números?')
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

#Verificando qual o menor, partindo da premissa que n1 seja o menor pra diminuir um "if"
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Verificando qual o maior, partindo da premissa que n3 seja o maior pra diminuir um "if"
maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2

#Exibindo o resultado
print('\n', '=*=' * 20)
print('Entre {}, {} e {}, {} é o maior e {} o menor.'.format(n1, n2, n3, maior, menor))
print('=*=' * 20, '\n')
