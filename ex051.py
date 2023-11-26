#LER 1º TERMO E RAZÃO DE PROGRESSÃO ARITMÉTICA (PA) E NO FINAL MOSTRAR OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO
t1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da progressão: '))
decimo = t1 + (10 - 1) * r

for c in range(t1, decimo + r, r):
    print(c)
