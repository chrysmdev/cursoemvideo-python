# DESAFIO 094
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média

pessoas = {}
total = []
soma = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip() .upper() [0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    total.append(pessoas.copy())
    while True:
        p = str(input('Deseja continuar? [S/N] ')).strip() .upper() [0]
        if p in 'SN':
            break
        print('ERRO! digite apenas S ou N.')
    if p == 'N':
        break
media = soma / len(total)

print('-=' * 30)
print(f'→ Foram cadastradas {len(total)} pessoa(s).') 
print(f'→ A idade média das pessoas é de {media} anos.')

print('→ As mulheres cadastradas foram: ', end = '')
for c in total:
    if c['sexo'] in 'F':
        print(f' {c["nome"]}', end = ';')
        
print()

print(f'→ As pessoas acima da média de {media:.1f} anos, são: ')
for v in total:
    if v['idade'] > media:
        print(f' - {v["nome"]} com {v["idade"]} anos')
print('<<< ENCERRADO >>>')
    
    
