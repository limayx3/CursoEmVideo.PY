#Ler nome e média de aluno, guardando também sua situação (aprovado/ reprovado) em um dicionário. no  fim mostrar conteúdo na tela
#"Nome é igual a XX, média é igual à XX, Situação é igual a XX."

pessoa = {}
pessoa['nome'] = str(input('Nome do aluno(a): '))
pessoa['média'] = float(input(f'Média do(a) {pessoa["nome"]}: '))
if 5 >= pessoa['média'] < 7:
    pessoa['situação'] = 'Recuperação'
elif pessoa['média'] >= 7:
    pessoa['situação'] = 'Aprovado'
else:
    pessoa['situação'] = 'Reprovado'

print(f'O aluno {pessoa['nome']} ficou {pessoa['situação']} por causa da média {pessoa['média']}.')
