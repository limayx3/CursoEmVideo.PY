#Programa com funçao voto() que recebe como parâmetro o ano de nascimento de alguém. Retorna um valor literal indicando se:
#Voto Negado, Opcional ou Obrigatório
from datetime import date

def voto(ano):
    hoje = date.today().year
    idade = 0
    situação = ''
    idade = hoje - ano
    if idade < 16:
        situação = 'Negado'
    elif 16 <= idade < 18:
        situação = 'Opcional'
    elif 18 <= idade <= 70:
        situação = '"Direito" Obrigatório'
    else:
        situação = 'Opcional pela experiência vivida'
    print(f'Com {idade} anos o voto é {situação}.')


nasc = int(input('Informe o ano de nascimento [AAAA]: '))
voto(nasc)
