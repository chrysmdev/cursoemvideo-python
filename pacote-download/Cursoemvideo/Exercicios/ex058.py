# DESAFIO 058
# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print('=-=-=-=-=-=-=- JOGO DA ADVINHAÇÃO -=-=-=-=-=-=-=')
print('Eu irei pensar em um número de 0 a 10\ne você tem que adivinhar em qual número pensei.')
sleep(2)
print('pensando...')
sleep(2)
escolhido = randint(0,10)
jogador = int(input('Digite qual número eu pensei: '))
tentativas = 1
print('-=' * 24)

while jogador != escolhido:
    print('você ERROU!!')
    if escolhido > jogador:
        print('pensei em um número maior...')
    else:
        print('pensei em um número menor...')
    jogador = int(input('tente novamente. Em qual número eu estou pensando? '))
    tentativas += 1
    print('-=' * 24)
    
print(f'Você ACERTOU!!! eu estava pensando no número {escolhido}, você teve {tentativas} tentativas até acertar.')
if tentativas == 1:
    print('VOCÊ FOI EXTRAORDINÁRIO!!! ')
elif tentativas <= 3:
    print('Você foi muito bem.')
elif tentativas <= 6:
    print('Você foi bem.')
else:
    print('você definitivamente tentou...')
'''
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual número qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou == True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
'''    