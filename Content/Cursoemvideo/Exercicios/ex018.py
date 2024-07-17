# DESAFIO 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
ang = float(input('Digite um valor de ângulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print(f'Para o ângulo {ang}\n Seu seno é: {seno:.2f} \n Seu cosseno é: {coss:.2f} \n Sua tangente é: {tang:.2f}')
