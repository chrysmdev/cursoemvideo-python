# DESAFIO 071
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual seraá o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que ao caixa possui cédulas de R$50, R$20, R$10 e R$1.

from time import sleep

print('-=-=-=-=-= CAIXA ELETRÔNICO =-=-=-=-=-')
valor = int(input('Digite o valor a ser sacado: R$ '))
c50 = 0
c20 = 0
c10 = 0
c1 = 0
while True:
    if valor > 0:
        while valor >= 50:
            valor -= 50
            c50 += 1
        while valor >= 20:
            valor -= 20
            c20 += 1
        while valor >= 10:
            valor -= 10
            c10 += 1
        while valor >= 1:
            valor -= 1
            c1 += 1
    else:
        break
print('Cédulas a serem impressas: ')
if c50 > 0:
    print(f'{c50} Cédulas de R$ 50,00')
if c20 > 0:
    print(f'{c20} Cédulas de R$ 20,00')
if c10 > 0:
    print(f'{c10} Cédulas de R$ 10,00')
if c1 > 0:
    print(f'{c1} Cédulas de R$ 1,00')
print('-=' * 20)
print('finalizando...')
sleep(2)
print('Volte sempre!')