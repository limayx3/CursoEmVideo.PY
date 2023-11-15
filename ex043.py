#DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOAL, CALCULE SEU IMC E MOSTRE SEU STATUS DE ACORDO COM A TABELA:
#ABAIXO DE 18.5 - ABAIXO DO PESO
#ENTRE 18.5 E 25 - PESO IDEAL
#ENTRE 25.1 E 30 - SOBREPESO
#ENTRE 31.1 E 40 - OBESIDADE
#ACIMA DE 40 - OBESIDADE MÓRBIDA

"""
1. Ler peso do usuário
2. Ler altura do usuário
3. Calcular IMC (peso / altura ** 2)
3.1. Se IMC < 18.5: Imprimir abaixo do peso
3.2. Se IMC >= 18.5 and <=25: Imprimir está no peso ideal
3.3. Se IMC >=25.1 and <=30: Imprimir está com sobrepeso
3.4. Se IMC >=30.1 and <=40: Imprimir está com obesidade, é melhor procurar uma junta médica para te ajudar.
3.5. Se IMC >40: Imprimir está com obesidade mórbida, procure uma junta médica urgente!
"""

print('\n####### CALCULADORA DE IMC #######')
peso = float(input('Informe o peso em kilogramas: '))
altura = float(input('Informe a altura em centimetros: '))

imc = peso / (altura / 100) ** 2

if imc < 18.5:
    print('{:.1f} - ABAIXO DO PESO IDEAL'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('{:.1f} - PESO IDEAL'.format(imc))
elif imc > 25 and imc <= 30:
    print('{:.1f} - SOBREPESO'.format(imc))
elif imc > 30 and imc <= 40:
    print('{:.1f} - OBESIDADE'.format(imc))
else:
    print('{:.1f} - OBESIDADE MÓRBIDA'.format(imc))

print('Seja qual for sua situação, enquanto há vida, há esperança. Procure ajuda médica e espiritual.')
