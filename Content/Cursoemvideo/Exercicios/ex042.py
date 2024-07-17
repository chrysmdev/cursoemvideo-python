# DESAFIO 042
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recuso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da segunda reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível formar um triângulo com essas retas.')
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO, pois possui todos os lados iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triângulo ISÓSCELES, pois possui 2 lados iguais')
    else:
        print('É um triângulo ESCALENO, pois possui todos os lados diferentes')
else:
    print('Não é possível formar o triângulo com essas retas.')
