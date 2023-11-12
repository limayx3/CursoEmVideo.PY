#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM E CALCULE O PREÇO DA PASSAGEM.
#R$0,50 POR KM PARA VIAGENS ATÉ 200KM E R$0,45 POR KM PARA VIAGENS MAIS LONGAS
distancia = int(input('Qual a distância de sua partida para sua chegada? Informe em km: '))
#CASO QUEIRA FAZER DO JEITO SIMPLIFICADO, AI O PRINT VIRIA DEPOIS.
#passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45
if distancia > 200:
    passagem1 = 0.45 * distancia
    print('O valor da sua passagem, à R$0,45 o km,  será R${}.'.format(passagem1))
else:
    passagem2 = 0.50 * distancia
    print('O valor da sua passagem, à R$0,50 o km, será R${}.'.format(passagem2))
