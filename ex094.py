#Ler nome, sexo e idade de váriaas pessoas. No fim mostrar: (A) Total de cadastros, (B) Média de idade do grupo, (C) Lista com as mulheres e
#(D) Lista com todos com idade acima dessa média.
pessoa = {}
cadastro = []
soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title().strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper().strip()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('Valor inválido. Digite F para FEMININO ou M para MASCULINO.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Dado inválido. Digite S para SIM e N para NÃO.')
    if continuar == 'N':
        break

print('='*30)
print(f'A → Cadastramos um total de {len(cadastro)} pessoas!')
média = soma / len(cadastro)
print(f'B → A média de idade é {média:5.2f} anos.')
print(f'C → As mulheres cadastradas foram: ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print(f'\nD → As pessoas com idade acima da média {média:5.2f} são: ', end='')
for p in cadastro:
    if p['idade'] > média:
        print(f'{p["nome"]} ', end='')
