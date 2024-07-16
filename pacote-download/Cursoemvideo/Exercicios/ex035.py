# DESAFIO 035
# Desenvolva um programa que eleia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da segunda reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível formar um triângulo com essas retas.')
else:
    print('Não é possível formar o triângulo com essas retas.')