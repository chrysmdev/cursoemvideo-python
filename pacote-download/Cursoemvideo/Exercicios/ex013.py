# DESAFIO 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o seu salário? R$ '))
novo = salario + (salario * 15/100)
print(f'Com o aumento de 15%, o seu novo salario é de R$ {novo}')