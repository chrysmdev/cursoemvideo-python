# DESAFIO 041
# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM 
# Até 14 anos: INFANTIL 
# Até 19 anos: JUNIOR 
# Até 25 anos: SÊNIOR 
# Acima: MASTER

from datetime import date

nome = str(input('Digite o nome do(a) atleta: ')).strip() .capitalize()
nascimento = int(input('Informe o ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print(f'{nome} tem {idade} anos e está na categoria MIRIM')
elif idade <= 14:
    print(f'{nome} tem {idade} anos e está na categoria INFANTIL')
elif idade <= 19:
    print(f'{nome} tem {idade} anos e está na categoria JUNIOR')
elif idade <= 25:
    print(f'{nome} tem {idade} anos e está na categoria SÊNIOR')
else:
    print(f'{nome} tem {idade} anos e está na categoria MASTER')