# DESAFIO 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

h = float(input('Qual a altura em metros da parede? '))
x = float(input('Qual a largura em metros da parede? '))
a = h * x
l = a / 2
print(f'Uma parede de {x}x{h} possui {a}m², logo será necessário {l} litros de tinta para pinta-la completamente.')
