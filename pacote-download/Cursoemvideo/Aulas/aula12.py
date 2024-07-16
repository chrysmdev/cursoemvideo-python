# AULA 12
# if se verdadeiro será realizado
# elif (else + if) serve como alternativa de if (se o if n for verdadeiro, o elif será testado)
# else caso if não seja verdadeiro, o else será realizado


nome = str(input('Qual é o seu nome? '))
if nome == 'Chrystian':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jéssica Juliana Rayssa':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um otimo dia, {nome}!')
    