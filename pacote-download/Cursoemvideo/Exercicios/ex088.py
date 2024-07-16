# DESAFIO 088
# Faça um programa que ajude um jogador da MEGA SENA a cria palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('-' * 52)
print(f'{" MEGA SENA ":^52}')
print('-' * 52)

jogos = int(input('Quantos jogos quer que eu sorteie? '))
sorte = []

print('=-' * 8, f' SORTEANDO {jogos} JOGOS', '-=' * 8)

for q in range(0, jogos):
    vezes = 0
    while True:
        r = randint(1, 60)
        if r not in sorte:
            sorte.append(r)
            vezes += 1
        if vezes == 6:
            break
    print(f'{q + 1}° jogo: {sorted(sorte)}')
    sleep(0.5)
    sorte.clear()

print('-=' * 26)