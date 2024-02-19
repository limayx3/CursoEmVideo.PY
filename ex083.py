#LER EXPRESSÃO NUMÉRICA QUALQUER QUE USE PARÊNTESES E INFORMAR SE É OU NÃO VÁLIDA, COM PARÊNTESES ABERTOS E FECHADOS NA ORDEM CORRETA.

exp = str(input('Digite uma expressão: '))

lista = []                                  #Todo str é uma lista, portanto podemos trabalhar com essa forma

for símbolo in exp:                         #para cada símbolo na expressão exp:
    if símbolo == '(':                      #pesquisar se ele é um '('
        lista.append('(')                   #adicioná-lo na lista
    elif símbolo == ')':                    #pesquisar se é um ')'
        if len(lista) > 0:                      #se o tamanho da lista for maior que 0
            lista.pop()                         #remover o último símbolo da lista
        else:
            lista.append(')')
            break

if len(lista) == 54/3(a+b(58-12)) = 30:
    print('Digitaste uma expressão válida.')
else:
    print('Marrapais, esqueceu uns parente hein... Prestenção!')
