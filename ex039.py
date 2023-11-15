#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME DE ACORDO COM SUA IDADE NO ANO ATUAL:
#(1) SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR (INFORMAR TAMBÉM QUANTO TEMPO FALTA)
#(2) SE É O ANO DE SEU ALISTAMENTO
#(3) SE JÁ PASSOU DO TEMPO DO ALISTAMENTO (INFORMAR TAMBÉM QUANTO TEMPO PASSOU)
#IMPORTAR BIBLIOTECA PRA PEGAR ANO ATUAL
"""
1. Importar biblioteca/ módulo datetime e usar função date (ano = date.today().year)
2. Ler ano de nascimento do rapaz
3. Verificar qual ano atual
4. Calcular idade do rapaz no ano atual
5.1. Se <=17: Informar quanto falta para se alistar
5.2. Se 18: Informar que precisa se alistar esse ano
5.3. Se >=19: Informar que já passou a data de alistamento e quanto passou
"""
from datetime import date

nasc = int(input('Em qual ano nasceu? '))
ano = date.today().year
idade = ano - nasc

if idade == 18:
    print('Nesse ano ({}) você completou ou completa 18 anos, portanto vá se alistar, calabrezo! Você só tem até 30 de junho!'.format(ano))
elif idade < 18:
    falta = 18 - idade
    print('Você ainda é garotinho juvenil, ainda não tem a idade necessária.')
    print('Mas fique atento, leite com pêra, você se alistará em {} ano(s), em {}.'.format(falta, ano + falta))
elif idade > 18:
    passou = idade - 18
    print('Você passou {} ano(s) da idade de se alistar, que foi em {}. Espero que tenha feito o procedimento correto, pitango.'.format(passou, ano - passou))
