#QUESTIONA QUANTOS N PRIMEIROS ELEMENTOS QUER QUE SEJA EXIBIDO DA SEQUENCIA DE FIBONACCI.
print('-' *30)
print('SeQuÊnCiA FiBoNaCcI')
print('-'*30)
termos = int(input('Quantos termos você quer ver? '))
t1 = 0
t2 = 1
print('\n{} → {} → '.format(t1, t2), end='')
c = 3

while c <= termos:
    t3 = t1 + t2
    print('{} → '.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1

print('FIM. \n')