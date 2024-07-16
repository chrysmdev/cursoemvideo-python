# DESAFIO 045
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep


desafio = str(input('Olá, te desafio a uma partida de jopenpo!\nVocê aceita o desafio? ')).strip() .upper()

if desafio == 'SIM':
    print('Existem 3 opções: A Pedra, O Papel e A Tesoura.\nAs regras são:\n Tesoura ganha do Papel\n Papel ganha da Pedra\n Pedra ganha da Tesoura.\n Você escolhará um e eu também, no fim iremos ver quem ganhou!')
    print('escolhendo...')
    sleep(3)
    print('EU JÁ ESCOLHI O MEU!!')
    seleção = str(input('Pedra\nPapel\nTesoura\nQual você escolhe? ')).strip() .upper()
    escolhacomp = ['PEDRA', 'PAPEL', 'TESOURA']
    escolhidocomp = choice(escolhacomp)
    if seleção == 'TESOURA' and escolhidocomp == 'PAPEL':
        print('PERDI!! eu escolhi Papel... você venceu o desafio, vou escolher melhor da proxima vez.')
    elif seleção == 'TESOURA' and escolhidocomp == 'PEDRA':
        print('GANHEI!!! eu escolhi Pedra! sou o campeão desse desafio, humanos não tem chance contra máquinas!')
    elif seleção == 'PAPEL' and escolhidocomp == 'TESOURA':
        print('GANHEI!!! eu escolhi Tesoura! sou o campeão desse desafio, humanos não tem chance contra máquinas!')
    elif seleção == 'PEDRA' and escolhidocomp == 'TESOURA':
        print('PERDI!! eu escolhi Tesoura... você venceu o desafio, vou escolher melhor da proxima vez.')
    elif seleção == 'PEDRA' and escolhidocomp == 'PAPEL':
        print('GANHEI!!! eu escolhi Papel! sou o campeão desse desafio, humanos não tem chance contra máquinas!')
    elif seleção == 'PAPEL' and escolhidocomp == 'PEDRA':
        print('PERDI!! eu escolhi Pedra... você venceu o desafio, vou escolher melhor da proxima vez.')
    else:
        print('Escolhemos iguais... acho que pensamos da mesma forma. Você é tão inteligente quanto eu.')
        
else:
    print('OK MEDROSO! pode fugir, eu irei procurar um oponente digno de me vencer!')

'''
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA')

jogador = int(input('Qual é sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]})
print('-=' * 11)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

'''