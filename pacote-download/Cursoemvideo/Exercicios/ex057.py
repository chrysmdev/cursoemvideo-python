# DESAFIO 057
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça para a digitação novamente até ter um valor correto.

sexo = str(input('Informe o seu sexo [M/F]: ')).strip() .upper() [0]
while sexo != 'M' or sexo != 'F':            # while sexo not in 'MmFf':
    sexo = str(input('Dado invalido. digite novamente o seu sexo [M/F]: ')).strip() .upper()
print('Dado coletado com sucesso. sexo: {sexo}')
