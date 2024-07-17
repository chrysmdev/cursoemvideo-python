# DESAFIO 101
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    global idade
    
    atual = date.today().year
    idade =  atual - ano
    
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIA'
    
    
    
# PROGRAMA PRINCIPAL
permissão = voto(int(input('Qual seu ano de nascimento? ')))
print(f'Com {idade} anos a sua situação de voto é: {permissão}')