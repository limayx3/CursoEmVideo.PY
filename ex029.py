#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM VEÍCULO.
#SE V>80KM/H, MOSTRE QUE FOI MULTADO E O VALOR DA MULTA, SENDO R$7,00 POR CADA KM ACIMA DO LIMITE.
"""
1. Ler velocidade do veículo
2. Calcular se foi ou não multado
3. Se multado calcular o valor
"""
print("""======================================================================================
      Olá motorista! Preciso que me diga à que velocidade você passou no km 281 da
      rodovia PY066, pois acho que estava muito rápido!\n======================================================================================""")
v = int(input('      Digite apenas o número inteiro da sua velocidade: '))
if v > 80:
    multa = float((v - 80) * 7)
    print("""======================================================================================
    Caramba, você estava à milhão! Vamos te enviar uma multa no valor de R${:.2f}.""".format(multa))
else:
    print("""======================================================================================
    Ufa! Você não estava acima da velocidade permitida. Direção defensiva!\n======================================================================================""")