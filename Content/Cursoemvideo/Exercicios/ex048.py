# DESAFIO 048
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
s = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            s += c
print(f'A soma entre todos os números ímpares múltiplos de 3 na faixa de 1 até 500 é: {s}')
'''

s = 0
c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += c
        c += 1
print(f'A soma entre todos os {c} valores solicitados é {s}')
