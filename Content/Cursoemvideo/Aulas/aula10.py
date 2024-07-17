# AULA 10

# if carro.esquerda():
#   bloco True
# else:
#   bloco False

'''
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')
'''

'''
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')
'''

'''
nome = str (input('Qual é seu nome? '))
if nome == 'Chrystian':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print(f'Bom dia, {nome}!')
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m}')
if m >= 6.0:
    print('Você está na média, PARABÉNS!')
else:
    print('Você está abaixo da média, estude mais!')