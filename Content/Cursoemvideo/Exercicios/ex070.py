# DESAFIO 070
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

print('{:=^40}'.format(' Loja Menezes '))
barato = ''
total = mil = anterior = 0
while True:
    produto = str(input('Nome do produto: ')).strip() .capitalize() 
    preço = float(input('Preço do produto: R$ '))
    total += preço
    if preço >= 1000:
        mil += 1
    if anterior == 0 or preço < anterior:
        anterior = preço
        barato = produto
    print('-=-' * 16)   
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja adicionar mais um produto [S/N]? ')).strip() .upper() [0]
    if pergunta == 'N':
        break
    print('-=-' * 16)
print(f'''-=-=-=-=- CAIXA -=-=-=-=-
Total a pagar = R$ {total:.2f}
{mil} produtos custam a partir de R$1000.00
{barato} foi o produto mais barato''')
