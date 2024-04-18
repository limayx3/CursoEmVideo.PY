#Programa com funçao voto() que recebe como parâmetro o ano de nascimento de alguém. Retorna um valor literal indicando se:
#Voto Negado, Opcional ou Obrigatório
def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if idade < 16:
        return f'Com {idade} anos: Voto Negado!'
    elif 16 <= idade < 18:
        return f'Com {idade} anos: Voto Opcional!'
    elif 18 <= idade <= 70:
        return f'Com {idade} anos: "Direito" Obrigatório kakaka.'
    else:
        return f'Com {idade} anos: Voto Opcional pela experiência vivida.'
    


nasc = int(input('Informe o ano de nascimento [AAAA]: '))
print(voto(nasc))
