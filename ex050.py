#LER 6 NÚMEROS INT, MOSTRAR A SOMA DE APENAS OS QUE FOREM PARES. SE VALOR DIGITADO FOR ÍMPAR, DESCONSIDERAR
s = 0 #variável acumuladora
contador = 0 #variável contadora
for c in range(1, 7): #0, 6 tmbém funciona, mas não mostra correto na frase do input
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        s += n #s = s + n
        contador += 1
print('O valor total da soma é: {}.'.format(s))
print('Tivemos {} valores pares.'.format(c))
