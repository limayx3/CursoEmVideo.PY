#LER SEXO DE PESSOA E SÓ ACEITE OS VALORES "M" E "F", PEDINDO NOVA DIGITAÇÃO ATÉ FAZEREM CERTO

sexo = str(input('Digite seu sexo: [M ou F] ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Que isso, helecóptero de guerra apaxe? Digite um dado válido: [M/F] ')).strip().upper()[0]

print('Que bom, você digitou corretamente, o sexo {} foi registrado com sucesso.'.format(sexo))
