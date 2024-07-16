# DESAFIO 097
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# ex:  escrava('Olá, Mundo!')
# saída:
# ~~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~~

def escreva(frase):
    limite = len(frase) + 4
    print('-' * limite)
    print(f'{frase:^{limite}}')
    print('-' * limite)


# PROGRAMA PRINCIPAL
escreva('Olá, Mundo!')