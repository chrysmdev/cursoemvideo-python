# DESAFIO 091
# Crie um programa onde 4 jogadores joguem um dado(1-6) e tenham resultador aleatórios. Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

dado = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}

print('Sorteando...')
sleep(0.5)
for k, v in dado.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
    
print('-=' * 20)
print(' == RANKING DOS JOGADORES ==')
for c in sorted(dado, key = dado.get, reverse = True):
    print(f'  → {c} com: {dado[c]}.')
print('-=' * 20)

# from operator import itemgetter
# raking = list()
# ranking = sorted(dado.items(), key = itemgetter(1), reverse = True)
