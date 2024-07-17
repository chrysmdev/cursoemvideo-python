# DESAFIO 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27

din = float(input('Quantos reais você possui em sua carteira? R$'))
print(f'Com R$ {din:.2f} você consegue adquirir US$ {din / 3.17:.2f}')