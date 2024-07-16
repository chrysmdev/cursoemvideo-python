# DESAFIO 086
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta
# linha / coluna  

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 20)

for p in matriz:
    print(f'[ {p[0]:^4} ] [ {p[1]:^4} ] [ {p[2]:^4} ] ')
