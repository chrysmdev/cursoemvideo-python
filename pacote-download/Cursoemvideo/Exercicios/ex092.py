# DESAFIO 092
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário 
# Se por acaso a CTPS for diferente de ZERO o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# 35 anos de contribuição

from datetime import date

dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho(digite 0 se n possuir): '))
if dados['ctps'] > 0:
    dados['contrato'] = int(input('Ano da Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = (dados['contrato'] + 35) - nascimento

print('-=' * 30)
for k, v in dados.items():
    print(f' → {k} tem valor {v}')
