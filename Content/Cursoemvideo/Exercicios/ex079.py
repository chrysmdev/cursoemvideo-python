# DESAFIO 079
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()
pergunta = ' '
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in valores:
        print('esse número já foi adicionado, tente outro.')
    else:
        valores.append(valor)
        print('Valor foi adicionado com sucesso')
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N] ')).strip() .upper() [0]
    if pergunta == 'N':
        break
    pergunta = ' '
print(f'Os valores adicionador foram: {sorted(valores)}')
