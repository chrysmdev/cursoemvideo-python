# DESAFIO 099
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior(lista):
    for k, v in enumerate(lista):
        if k == 0:
            maior = v
        else:
            if maior < v:
                maior = v
    print(maior)


# PROGRAMA PRINCIPAL
lista = []

while True:
    lista.append(int(input('Adicione um valor: ')))
    while True:
        r = str(input('Deseja adicionar mais um valor[S/N]? ')).strip() .upper() [0]
        if r in 'SN':
            break
    if r == 'N':
        break

maior(lista)
'''
from time import sleep

def maior(* valor):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in valor:
        if cont == 0:
            maior = n
        else:
            if maior < n:
                maior = n
        print(n, end = ' ', flush = True)
        sleep(0.3)
        cont += 1
    print(f'foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# PROGRAMA PRINCIPAL
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()