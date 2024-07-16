# DESAFIO 074
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de número gerados e também indique o menor e o maior valor que estão na tupla.

from random import sample

print(f'{" Gerador de números ":-^60}')
num = tuple(sample(range(100), 5))
print(f'Os 5 números aleatorios gerados foram: {num[0]}, {num[1]}, {num[2]}, {num[3]}, {num[4]}')
print('-=' * 30)

for c in range(0, 5):
    if c == 0:
        maior = num[0]
        menor = num[0]
    else:
        if maior < num[c]:
            maior = num[c]
        if menor > num[c]:
            menor = num[c]
            
print(f'O maior valor dentre os 5 gerados foi: {maior}')
print('-=' * 30)
print(f'O mehnor valor dentre os 5 gerados foi: {menor}')

'''
from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {num}')
print(f'O maior valor sortedo foi {max(num)}')
print(f'O menor valor sortedo foi {min(num)}')
'''