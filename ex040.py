#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉRIA, MOSTRANDO UMA MENSAGEM DE ACORDO COM A MÉDIA ATINGIDA:
#ABAIXO DE 5.0 - REPROVADO
#DE 5.0 À 6.9 - RECUPERAÇÃO
#7.0 OU ACIMA - APROVADO
#(MINHA INVENÇÃO) - SE MÉDIA 9.5 OU ACIMA DIZER QUE ESTÁ DE PARABÉNS PELA DEDICAÇÃO
"""
1. Ler nota1
2. Ler nota2
3. Calcular média
4.1. Se média <5: REPROVADO
4.2. Se média >=5 and <=6.9: RECUPERAÇÃO
4.3. Se média >=7: APROVADO
4.3.1. Se média >=9.5: Parabenizar dedicação
"""

aluno = str(input('Informe o nome do aluno: '))
matéria = str(input('Informe a matéria em questão: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2

if média < 5:
    print('Sua média em {} foi {}, {}. Você está REPROVADO, bicho burro.'.format(matéria, média, aluno))
elif média >= 5 and média < 7:
    print('{}, em {} sua média foi {}, tão apertado quanto o sutiã da Thais Karla. Você está em RECUPERAÇÃO, estuda hein!'.format(aluno, matéria, média))
elif média >= 7:
    print('PARABÉNS, {}. Você está APROVADO em {} com média {}.'.format(aluno, matéria, média))
    if média >= 9.5:
        print('Melhor ainda, você se dedicou e essa média é resultado de muito esforço! Continue assim!')
print('Lembre-se: O meio seleciona o mais apto.')
