# DESAFIO 095
# Aprimere o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamente de cada jogador.
time = []
dados = {}
gols = []
total = 0

while True:
    dados.clear()
    gols.clear()
    dados['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input('Quantidade de partidas jogadas no campeonato: '))
    for q in range(1, partidas + 1):
        gol = int(input(f'Quantidade de gol(s) marcado(s) na {q}° partida: '))
        total += gol
        gols.append(gol)
    dados['gols'] = gols[:]
    dados['total'] = total
    time.append(dados.copy())
    while True:
        r = str(input('Deseja adicionar mais um jogador? [S/N] ')).strip() .upper() [0]
        if r in 'SN':
            break
    if r == 'N':
        break
    
print('-' * 40)

print('cod ', end = '')
for i in dados.keys():
    print(f'{i:<15}', end = '')

print()
print('-' * 40)

for k, v in enumerate(time):
    print(f'{k:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()

print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERROR!! Não existe o jogador com código {busca}! tente novamente.')
    else:
        print(f' -- LEVANTAMENTE DO JOGADOR {time[busca] ["nome"]}:')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 40)

print('<< VOLTE SEMPRE >>')
