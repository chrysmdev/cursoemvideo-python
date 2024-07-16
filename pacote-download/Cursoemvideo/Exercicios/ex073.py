# DESAFIO 073
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) apenas os 5 primeiros colocados.
# B) O últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.


time = ('Botafogo', 'Palmeiras', 'Gremio', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Flamengo', 'Fortaleza', 'Atlético-MG', 'Corinthians', 'Cuiabá', 'Cruzeiro', 'Internacional', 'São Paulo', 'Vasco da Gama', 'Goiás', 'Bahia', 'Santos', 'América-MG', 'Coritiba')
print('-=' * 55)
print(f'Os primeiros colocados são: (1°) {time[0]}, (2°) {time[1]}, (3°) {time[2]}, (4°) {time[3]}, (5°) {time[4]}.')
print('-=' * 55)
print(f'Na zona de rebaixamento está: (17°) {time[-4]}, (18°) {time[-3]}, (19°) {time[-2]}, (20°) {time[-1]}.')
print('-=' * 55)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-=' * 55)
n = str(input('Digite um time para ver a posição especifica: ')).strip() .capitalize()
print(f'O {n} está na: {time.index(n) + 1}° posição')