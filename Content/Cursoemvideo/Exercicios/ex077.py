# DESAFIO 077
# Crie um programa que tenha uma tupla com várias palavras (não use acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('CASAR', 'VIVER', 'PROGRAMAR', 'FELICIDADE', 'GARRAFA', 'SORRIR', 'TRABALHAR', 'AMIZADE', 'FAMILIA', 'PYTHON', 'ESTUDAR', 'FUTURO')

for n in palavras:
    print(f'\na palavra {n} tem as vogais: ', end = '')
    if 'A' in n:
        print('A', end = ' ')
    if 'E' in n:
        print('E', end = ' ')
    if 'I' in n:
        print('I', end = ' ')
    if 'O' in n:
        print('O', end = ' ')
    if 'U' in n:
        print('U', end = ' ')

'''
palavras = ('CASAR', 'VIVER', 'PROGRAMAR', 'FELICIDADE', 'GARRAFA', 'SORRIR', 'TRABALHAR', 'AMIZADE', 'FAMILIA', 'PYTHON', 'ESTUDAR', 'FUTURO')
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = '')
'''