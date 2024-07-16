# DESAFIO 083
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e fechados na ondem correta.
'''
frase = str(input('Digite uma expressão númerica: '))
if frase.count('(') == frase.count(')'):
    print('Essa expressão é possivel')
else:
    print('essa expressão é invalida')
'''

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')