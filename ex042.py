#REFAÇA O DESAFIO 35 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
#EQUILÁTERO - 3 LADOS IGUAIS
#ISÓSCELES - DOIS LADOS IGUAIS
#ESCALENO - TODOS OS LADOS DIFERENTES
"""
0. VERIFICAR EXERCÍCIO 35 PRA FACILITAR
1. Ler 3 segmentos
2. Calcular se os segmentos informados formam um triângulo
2.1. Se 3 segmentos iguais: Equilátero
2.2. Se 2 segmentos iguais: Isósceles
2.3. Se nenhum segmento igual: Escaleno
2.4. Se não formar triângulo, informar ao usuário.
"""
s1 = float(input('Informe o valor do segmento 1: '))
s2 = float(input('Informe o valor do segmento 2: '))
s3 = float(input('Informe o valor do segmento 3: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 == s3: #Condição funciona bem no python! UHUL!
        print('Com os segmentos {}, {} e {} formamos um triângulo EQUILÁTERO.'.format(s1, s2, s3))
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('Com os segmentos {}, {} e {} formamos um triângulo ISÓSCELES.'.format(s1, s2, s3))
    elif s1 != s2 != s3 != s1:
        print('Com os segmentos {}, {} e {} formamos um triângulo ESCALENO.'.format(s1, s2, s3))
else:
    print('Com os segmentos {}, {} e {} NÃO formamos um triângulo.'.format(s1, s2, s3))

print('Bons estudos!\n')