# DESAFIO 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice
numusu = int(input('Escolha um número de 0 a 5: '))
num = [0, 1, 2, 3, 4, 5]
escolhido = choice(num)
if escolhido == numusu:
    print(f'VENCEU!! Parabéns!! o seu número foi {numusu} e o computador escolheu o mesmo.')
else:
    print(f'PERDEU!! Infelizmente o {numusu} não foi o número escolhido, o número escolhido foi {escolhido}')
    
'''
from randon import randint
from time import sleep
computador = radint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS, Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!' .format(computador, jogador))
'''