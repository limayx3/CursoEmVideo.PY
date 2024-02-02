#LER IDADE E SEXO DE VÁRIAS PESSOAS, QUESTIONANDO SE QUER CADASTRAR MAIS UM A CADA FIM DE CADASTRO.
#NO FIM MOSTRAR: (1) QUANTOS TEM MAIS DE 18 ANOS, (2) QUANTOS HOMENS FORAM CADASTRADOS E (3) QUANTAS MULHERES TEM MENOS DE 20 ANOS.

idade = maior = homem = mulher = 0
continuar = sexo = 'S'

while True:
    continuar = str(input('Você quer adicionar um cadastro? [N para parar] ')).strip().upper()[0]
    if continuar == 'N':
        break

    idade = int(input('Digite idade da pessoa: '))
    sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    elif sexo == 'M':
        homem += 1
    else:
        if idade < 20:
            mulher += 1

print('=' * 50)
print(f'''Cadastro finalizado com sucesso.\nVocê adicionou {maior} maiores de idade, {homem} homem(ns)\ne {mulher} mulher(es) com menos de 20 anos.''')
print('=' * 50)
