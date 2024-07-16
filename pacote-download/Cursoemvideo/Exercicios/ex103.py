# DESAFIO 103
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha o jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols != int():
        gols =  0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# PROGRAMA PRINCIPAL

jogador = str(input('Nome do jogador: ')).strip() .capitalize()
gol = input('Número de gols: ')

ficha(jogador, gol)