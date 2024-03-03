#Ler nome e 2 notas de vários alunos, guardando tudo em uma lista composta: [listona com tudo[listinha com nome e [listinha com 2 notas]][listinha com nome e [listinha com 2 notas]]...]
#No fim mostrar tabela com ordem numérica de insersão, nomes e médias, também permitir mostrar a nota de cada aluno, dando a opção 999 para parar.

listagem = list()
aluno = list()
notas = list()
cont = 0
média = 0

while True:
    nome = str(input('Nome do aluno: '))
    aluno.append(nome[:])
    for c in range (0, 2):
        nota = float(input('Informe a nota: '))
        notas.append(nota)
    média = (notas[0] + notas[1]) / 2
    notas.append(média)
    aluno.append(notas[:])
    listagem.append(aluno[:])
    notas.clear()
    aluno.clear()
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in "Nn":
        break
print(f'Foram cadastrados um total de {cont} alunos.\n')    
print(f'{"POS":<5}{"NOME":^35}{"MÉDIA":^10}')
for c in range (0, len(listagem)):
    print(f'{(c+1):>2}º {listagem[c][0]:^35}{listagem[c][1][2]:^10.2f}')

while True:
    num = (int(input('Escolha um aluno para exibir as notas individuais:\n[999 para sair] ')))
    if num == 999:
        print('FECHANDO O SISTEMA...')
        break
    print(f'A média do aluno {listagem[num-1][0]} foi composta pelas notas {listagem[num-1][1][0]} e {listagem[num-1][1][1]}')

print('Valeu, falou.')
