# DESAFIO 068
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('~~' * 11, 'Ímpar ou Par', '~~' * 11)
print('''Você deve escolher entre ímpar ou par e depois dizer um número.
O meu número será somado com o seu número de escolha.
Se a soma for de acordo com o que você escolheu, você ganha.
O programa para quando você perder.''')
vezes = 0
while True:
    print('-=' * 30)
    computer = randint(0, 9)
    choice = ' '
    while choice not in 'íip':
        choice = str(input('Escolha entre ímpar ou par: ')).strip() .lower() [0]
    user = int(input('Digite o seu número: '))
    result = (computer + user) % 2
    if choice in 'íip':
        if result == 0:
            print(f'eu escolhi {computer} ou seja, o resultador é PAR')
            if choice == 'p':
                print('parabéns você GANHOU')
                vezes += 1
            else:
                break
        else:
            print(f'eu escolhi {computer} ou seja, o resultador é ÍMPAR')
            if choice in 'íi':
                print('parabéns você GANHOU')
                vezes += 1
            else:
                break
print ('-=' * 30)
print (f'Você PERDEU. Foram {vezes} vitórias conquistadas')