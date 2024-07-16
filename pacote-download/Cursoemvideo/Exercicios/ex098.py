# DESAFIO 098
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada.

from time import sleep

def contador(inicio, fim, passo):
    print(f'Contando de {inicio} até {fim} pulando de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if inicio > fim:
        if passo > 0:
            passo = -passo
        for n in range(inicio, fim - 1, passo):
            print(n, end = ' ', flush = True)
            sleep(0.1)
    if inicio < fim:
        for n in range(inicio, fim + 1, passo):
            print(n, end = ' ', flush = True)
            sleep(0.1)
    print('FIM')
    print('-' * 30)


def cab(a):
    print('-' * 30)
    print(f'{a:^30}')
    print('-' * 30)


# PROGRAMA PRINCIPAL
cab('FUNÇÃO DE CONTADOR')

contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))