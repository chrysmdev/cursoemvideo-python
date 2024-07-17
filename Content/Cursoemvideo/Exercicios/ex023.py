# DESAFIO 023

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('Digite um valor de 0 a 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print(f'Analisando o número {num}')
print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mil}')
