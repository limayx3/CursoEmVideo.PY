#FAÇA UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E MOSTRE:
#(1) QUANTAS VEZES APARECE A LETRA 'A', (2) EM QUE POSIÇAO ELA APARECE A PRIMEIRA VEZ, (3) EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

frase = str(input('Digite uma frase qualquer: ')).strip()
peq = frase.lower()
print('A frase digitada foi "{}" e nela temos:'.format(frase))
print('Temos {} letras "a" nessa frase, sendo a primeira na posição {} e a última em {}.'.format(peq.count('a'), peq.find('a')+1, peq.rfind('a')+1))
