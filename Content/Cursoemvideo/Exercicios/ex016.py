# DESAFIO 016
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# EX: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.

from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor foi {num} e o seu valor inteiro é {trunc(num)}')

'''
num = float(input('Digite um valor: '))
print(f'O valor foi {num} e o seu valor inteiro é {int(num)}')
'''

'''num = float(input('Digite um valor: '))
print(f'O valor foi {num} e o seu valor inteiro é {num:.0f}')
'''