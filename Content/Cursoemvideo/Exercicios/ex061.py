# DESAFIO 061
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Digite o termo desejado: '))
razão = int(input('Digite a razão: '))
final = 10
while final != 0:
    print(termo)
    termo += razão
    final -= 1


'''
print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro 
cont = 1
while cont <= 10:
    print(f'{termo} → ', end = '')
    termo += razão
    cont += 1
print('FIM')
'''