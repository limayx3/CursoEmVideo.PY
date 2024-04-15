#Criar uma função área() que receba largura e comprimento de um terreno retangular e mostre a área do terreno.

def área(base, altura):
    a = base * altura
    print(f'A área do terreno é {a:.2f}m²')


print(f'{" CÁLCULO DE ÁREA ":=^60}')
print(f'{" TERRENO RETANGULAR ":=^60}')
while True:
    continuar = str(input('Você deseja realizar o cálculo? [S/N] ')).upper().strip()[0]
    if continuar == 'S':
        b = float(input('Informe a base do terreno em metros: '))
        h = float(input('Informe a altura do terreno em metros: '))
        área(b, h)
    if continuar == 'N':
        break
