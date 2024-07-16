# DESAFIO 033
# faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
a = int(input('Digite o valor do primeiro número: '))
b = int(input('Digite o valor do segundo número: '))
c = int(input('Digite o valor do terceiro número: '))
# verificando menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando maior
maior =  a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O MAIOR valor é {maior}')
print(f'O MENOR valor é {menor}')

