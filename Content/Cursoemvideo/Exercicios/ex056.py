# DESAFIO 056
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

soma = 0
idadem = 0
nomem = ''
numf = 0
for c in range(1, 5):
    print(f'-=-=-= {c}° PESSOA -=-=-=')
    nome = str(input(f'NOME: ')).strip() .capitalize()
    idade = int(input(f'IDADE: '))
    sexo = str(input(f'SEXO [M/F]: ')).upper() .strip()
    soma += idade
    if sexo == 'M' and idade > idadem:
        idadem = idade
        nomem = nome
    if sexo == 'F' and idade < 20:
        numf = numf + 1
media = soma / 4
print(f'''A média de idade do grupo é de {media:.1f} anos;
O homem mais velho se chama {nomem} e tem {idadem} anos;
{numf} mulheres tem menos de 20 anos.''')
