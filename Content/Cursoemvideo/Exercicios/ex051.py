# DESAFIO 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA(progressão aritmética). no final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da progressão aritmética: '))
decimo = termo + (10 - 1) * razão
for c in range(termo, decimo + razão, razão):
    print(f'{c}', end = ' → ')
print('ACABOU') 