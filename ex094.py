#Ler nome, sexo e idade de váriaas pessoas. No fim mostrar: (A) Total de cadastros, (B) Média de idade do grupo, (C) Lista com as mulheres e
#(D) Lista com todos com idade acima dessa média.
pessoa = {}
cadastro = []
soma = média = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).title().strip()
    pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper().strip()[0]
    if pessoa['sexo'] not in 'FM':
        pessoa['sexo'] = str(input('Informação incorreta.\nFavor digitar F para feminino ou M para masculino: ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('='*30)
print(f'A → Cadastramos um total de {len(cadastro)} pessoas!')
média = soma / len(cadastro)
print(f'B → A média de idade é {média} anos.')
print(f'C → As mulheres cadastradas foram:')
for p in cadastro:
    for k, v in p.items():
        if pessoa['sexo'] == 'F':
            print(f'{v} ', end="")

