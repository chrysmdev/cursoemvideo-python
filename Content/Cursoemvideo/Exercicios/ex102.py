# DESAFIO 102
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show. 
# que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cáculo do fatorial.
# show por padrão é falso e coloque uma docstring

def fatorial(num, show = False):
    '''
    → Função que mostra o fatorial do número desejado, podendo ou não mostrar o processo da conta. Por padrão não mostra o processo.
    :param num: número a ser fatorado
    :param show: (opcional) mostra o processo de fatorização
    :return: sem return
    '''
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f


# PROGRAMA PRINCIPAL
print('-' * 30)
a = int(input('Digite um valor: '))
print(fatorial(a, show = True))