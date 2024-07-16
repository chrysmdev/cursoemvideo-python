# DESAFIO 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -Se ele ainda vai se alistar ao serviço militar
# -Se é a hora de se alistar.
# -Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou passou do prazo,

from datetime import date

nascimento = int(input('Digite o ano em que você nasceu: '))
ano = date.today().year
idade = ano - nascimento

if idade < 18:
    falta = 18 - idade
    print(f'Você ainda é jovem demais! Deverá se alistar no serviço militar no ano de {nascimento + 18}, ainda falta(m) {falta} ano(s) para você se apresentar.')    
elif idade > 18:
    passou = idade - 18
    print(f'Você passou do prazo! Deveria se alistar no serviço militar no ano de {nascimento + 18}, se passou {passou} ano(s), corra para a Junta de Serviço Militar mais proxima de você!')   
else:
    print(f'Você foi convocado para se apresentar a Junta de Serviço Militar mais proxima, para o alistamento militar desse ano. É HORA DE SE ALISTAR!')