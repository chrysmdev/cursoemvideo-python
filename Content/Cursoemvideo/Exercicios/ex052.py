# DESAFIO 052
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# 2 3 5 7 
'''
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    if num == 2:
        print('esse número é primo')
    else:
        print('esse número não é primo.')
elif num % 3 == 0:
    if num == 3:
        print('esse número é primo')
    else:
        print('esse número não é primo.')
elif num % 5 == 0:
    if num == 5:
        print('esse número é primo')
    else:
        print('esse número não é primo.')
elif num % 7 == 0:
    if num == 7:
        print('esse número é primo')
    else:
        print('esse número não é primo.')
else:
    print('esse número é primo')
'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end = ' ')
        tot += 1
    else:
        print('\033[31m', end = ' ')
    print(c, end = ' ')
print(f'\nO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('e por isso que ele É PRIMO.')
else:
    print('e por isso que ele NÃO É PRIMO!')
