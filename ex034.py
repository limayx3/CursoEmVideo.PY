#ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO E CALCULE O VALOR DE SEU AUMENTO.
#PARA SALÁRIOS > R$1250,00, AUMENTO DE 10%. PARA INFERIORES OU IGUAIS, AUMENTO DE 15%.

salario = float(input('\nQual salário vamos verificar? Digite apenas os números: R$'))
if salario > 1250:
    a1 = salario * 0.10
    print('Para o salário {:.2f}, teremos 10 porcento de aumento (R${:.2f}), totalizando R${:.2f}.\n'.format(salario, a1, (salario + a1)))
else:
    a2 = salario * 0.15
    print('Para o salário {:.2f}, teremos 15 porcento de aumento (R${:.2f}), totalizando R${:.2f}.\n'.format(salario, a2, (salario + a2)))
