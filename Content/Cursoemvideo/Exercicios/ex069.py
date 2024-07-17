# DESAFIO 069
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

from time import sleep
maior = 0
homens = 0
mulher20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip() .upper() [0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja adicionar mais pessoas [S/N]: ')).strip() .upper() [0]
    if pergunta == 'N':
        break
print('Finalizando programa...')
sleep(2)
print(f'''Você adicionou:
→ {maior} pessoas maiores de idade.
→ {homens} homens.
→ {mulher20} mulheres com menos de 20 anos.''')