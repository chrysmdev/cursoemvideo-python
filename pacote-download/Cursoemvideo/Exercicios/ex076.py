# DESAFIO 076
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços organizando os dados em forma tabular.
# ex: listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90)
print('-' * 50)
print(f'{" LISTAGEM DE PREÇO ":^50}')
print('-' * 50)

listagem = 'Filé de Peito de Frango', 13.49, 'Leite Líquido 1L', 4.29, 'Flocão de Milho', 1.99, 'Extrato de Tomate', 3.79, 'Pão de Queijo', 12.80, 'Feijão Carioca', 5.99, 'Creme dental', 2.49
for n in range(0, len(listagem)):
    if n % 2 == 0:
        print(f'{listagem[n]:.<41}', end = '')
    else:
        print(f'R$ {listagem[n]:>5.2f}')
print('-' * 50)