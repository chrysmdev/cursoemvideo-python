# DESAFIO 096
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.
def cab(a):
    print('-' * 30)
    print(f'{a:^30}')
    print('-' * 30)
    
    
def area(l, c):
    print(f'A área do terreno retangular é de {l * c} m²')


# PROGRAMA PRINCIPAL
cab('CALCULAR ÁREA')
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
