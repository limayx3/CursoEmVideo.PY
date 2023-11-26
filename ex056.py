#LER NOME, IDADE E SEXO DE 4 PESSOAS E MOSTRAR (1) MÉDIA DE IDADE DO GRUPO, (2) NOME DO HOMEM MAIS VELHO E (3) QUANTAS MULHERES TEM MENOS DE 21 ANOS

soma = 0
med = 0
nomemaisvelho = ''
idademaisvelho = 0
mulheresnovas = 0

#Ao colocar "ifs" dentro do laço, eles serão conferidos em cada iteração

for p in range( 1, 5):
    print('========== {}ª PESSOA =========='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F/ M): ')).strip().upper()
    soma += idade
    if p == 1 and sexo == 'M':
        nomemaisvelho = nome
        idademaisvelho = idade
    if idade > idademaisvelho and sexo == 'M':
        nomemaisvelho = nome
        idademaisvelho = idade
    if sexo == 'F' and idade < 20:
        mulheresnovas += 1

med = soma / 4
print('A média de idade do grupo é de {} anos.'.format(med))
print('O homem mais velho possui {} anos e se chama {}.'.format(idademaisvelho, nomemaisvelho))
print('Temos nessa lista {} mulheres com menos de 20 anos.'.format(mulheresnovas))
