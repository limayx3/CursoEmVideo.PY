#CALCULAR E MOSTRAR SOMA DOS NÚMEROS ÍMPARES MULTIPLOS DE 3 ENTRE 1 E 500.
s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        #print(c)
        s += c
print('A soma final desses algarismos é {}.'.format(s))
