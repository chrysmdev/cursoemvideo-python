# DESAFIO 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual o valor do produto? R$ '))
novo = preço - (preço * 5/100)
print(f'O seu produto está em promoção de 5% de desconto, agora por R$ {novo:.2f}')