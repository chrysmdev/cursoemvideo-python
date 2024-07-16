# DESAFIO 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo, calcule e mostre o comprimento da hipotenusa.

'''
co = float(input('O valor do cateto oposto é: '))
ca = float(input('O valor do cateto adjacente é: '))
hi = (co**2 + ca**2)**(1/2)
print(f'O valor da hipotenusa é: {hi:.2f}')
'''
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print(f'O valor da hipotenusa é: {hi:.2f}')
