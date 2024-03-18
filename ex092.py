#Ler nome, ano de nascimento (cadastrar a idade) e CTPS, cadastrando em um dicionário. Se CTPS diferente de 0 (zero), também questionar
#Ano de contratação e salário. Calcule e acrescente com quantos anos a pessoa vai se aposentar.
from datetime import date

pessoa = {}
hoje = date.today()
print(hoje)

pessoa['nome'] =str(input('Informe o nome: '))
nascimento = int(input('Ano de nascimento: [aaaa] '))
pessoa['idade'] = hoje.year - nascimento
pessoa['ctps'] = int(input('Informe a CTPS: [0 em caso negativo] '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Informe o ano de contratação: [aaaa] '))
    pessoa['salário'] = float(input('Informe seu salário: R$'))
    pessoa['aposentadoria'] = pessoa['contratação'] + 35

for k, v in pessoa.items():
    print(f'{k} = {v}')
if pessoa['ctps'] == 0:
    print('Esse vagal sem carteira deve morar com os pais. Fim do programa.')
else:
    print('Fim do programinha, vai trabalhar muito tempo ainda coitado(a).')