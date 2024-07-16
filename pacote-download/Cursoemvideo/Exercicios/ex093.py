# DESAFIO 093
# Crie um programa que gerencie o aproveitamente de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quatidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = {}
gols = []
total = 0
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantidade de partidas jogadas no campeonato: '))
for q in range(1, partidas + 1):
    gol = int(input(f'Quantidade de gol(s) marcado(s) na {q}° partida: '))
    total += gol
    gols.append(gol)
dados['gols'] = gols[:]
dados['total'] = total

print('-=' * 30)

print(dados)

print('-=' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
    
print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {partidas} partidas')
for c, v in enumerate(gols):
    print(f'  → Na {c + 1}° partida, fez {v} gols.')
print(f'Marcando assim {dados["total"]} gols.')
