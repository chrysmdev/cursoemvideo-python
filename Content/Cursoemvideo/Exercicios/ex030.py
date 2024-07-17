# DESAFIO 030
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número para saber se ele é ímpar ou par: '))
resultado = num % 2
if resultado == 0:
    print(f'O {num} é um número PAR!')
else:
    print(f'O {num} é um número ÍMPAR!')