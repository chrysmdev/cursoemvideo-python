# DESAFIO 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

nome = str(input('Seja bem-vindo ao aprovador de empréstimo, iremos analisar sua situação. \nInforme os dados necessários. \nQual o seu nome completo? ')).strip()
valorcasa = float(input('Qual o valor da casa que deseja adquirir? R$'))
salario = float(input('Qual o seu salário atual? R$'))
anos = int(input('E em quantos anos deseja pagar? '))
parcela = valorcasa / (anos * 12)
validador = salario * 30 / 100

if parcela > validador:
    print(f'{nome} a parcela de R${parcela:.2f} é acima que 30% do seu atual salário, então o seu emprestimo foi NEGADO!')
else:
    print(f'PARABÉNS!!! seu emprestimo foi aprovado! o valor de sua prestação será de R${parcela:.2f}')
