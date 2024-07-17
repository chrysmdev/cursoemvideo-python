# DESAFIO 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do sálario: '))
if salario > 1250:
    aumento = salario * 10 / 100
    novo = salario + aumento
else:
    aumento = salario * 15/100
    novo = salario + aumento
print(f'O atual salário é R$ {salario:.2f} e receberá um aumento de R$ {aumento:.2f} passando para um total de R$ {novo:.2f}')