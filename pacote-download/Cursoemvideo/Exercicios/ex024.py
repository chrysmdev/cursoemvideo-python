# DESAFIO 024

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cid = str(input('Digite o nome de sua cidade: ')).strip
cid = cid.upper()
cid = cid.split()
teste = 'SANTO' in cid[0]
print(f'Sua cidade começa com Santo? {teste}')
