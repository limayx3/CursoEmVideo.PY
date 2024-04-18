#Programa com função "fatorial()" que recebe 2 parâmetros: 1º númer a calcular o fatorial e 2º chamado show, sendo valor lógico opcional
# que indica se o cálculo do fatorial será mostrado (True) ou apenas o resultado (false). Tem que ter docstring

def fatorial(núm, show=1):
    '''
    Função utilizada para cálculo de fatorial de um número.
    param: núm - Indica valor a ser calculado fatorial
    param: show (opicional) - Valor booleado que indica necessidade de ver (True) ou não ver (False ou none) o cálculo.
    '''
    resultado = núm
    print(f'{núm}! = {núm} ', end="")
    
    if show == True:
        for c in range(núm-1, 0, -1):
            resultado *= c
            print(f'x {c} ', end="")
        print(f'= {resultado}')
    else:
        for c in range(núm-1, 0, -1):
            resultado *= c
        print(f'{núm}! = {resultado}')


escolha = int(input('Informe o número que deseja calcular o fatorial: '))
mostrar = str(input('Visualizar cálculo?: [S/N] ')).strip().upper()[0]
if mostrar == 'S':
    opção = True
if mostrar == "N":
    opção = False
fatorial(escolha, opção)
