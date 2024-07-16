# DESAFIO 031
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e RS0,45 para viagens mais longas.

distancia = float(input('Qual a distância até o destino em km? '))
if distancia <= 200:
    preço =  distancia * 0.50
else:
    preço = distancia * 0.45
print(f'Para {distancia} km o valor da passagem será de R$ {preço:.2f}')
