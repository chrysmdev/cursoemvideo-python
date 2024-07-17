# DESAFIO 062
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite o termo desejado: '))
razão = int(input('Digite a razão: '))
final = 10
pergunta = ''
while pergunta != 0:
    print(f'{termo} → ', end = '')
    termo += razão
    final -= 1
    if final == 0:
        print('PAUSA')
        pergunta = int(input('Quantos termos deseja ver? '))
        if pergunta > 0:
            final = pergunta      
print('FIM')
            
