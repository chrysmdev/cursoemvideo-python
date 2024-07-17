# DESAFIO 050
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for ímpar, desconsidere-o.
'''
s = 0
for c in range(0, 6):
    n1 = int(input('Digite um número inteiro: '))
    if n1 % 2 == 0:
        s += n1
print(s)
'''

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        soma += num
        cont =+ 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')