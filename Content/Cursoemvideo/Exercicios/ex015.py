# DESAFIO 015
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Por quantos km você dirigiu o carro? '))
t = dias * 60
d = km * 0.15
print(f'Após {dias} dias você dirigiu o carro por {km} km e terá que pagar um aluguel de R$ {t + d:.2f}')