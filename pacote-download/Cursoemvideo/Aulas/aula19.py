# AULA 19
# DICIONÁRIOS
'''
dados = dict()
dados = {}

dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])     #Pedro
print(dados['idade'])    #25

# ADICIONANDO ELEMENTOS

dados['sexo'] = 'M'

# ELIMINANDO ELEMENTOS

del dados['idade']

#

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

print(filme.values()) #dict_values(['Star Wars', 1977, 'George Lucas'])
print(filme.keys())   #dict_keys(['titulo', 'ano', 'diretor'])
print(filme.items())  #dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

for k, v in filme.items():
    print(f'O {k} é {v}')   # O titulo é Star Wars  # O ano é 1977 # O diretor é George Lucas
    
locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},{'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}, {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]
print(locadora[0]['ano']) # 1977
print(locadora[2]['titulo']) # Matrix
'''
# AULA PRATICA
'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
for k in pessoas.keys():
    print(k)    # nome  sexo  idade
for k in pessoas.values():
    print(k)    # Gustavo  M  22
for k, v in pessoas.items(): # items substitui enumerate
    print(f'{k} = {v}') # nome = Gustavo  sexo = M  idade = 22

pessoas['peso'] = 98.5
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}') # nome = Leandro  sexo = M  idade = 22  peso = 98.5
'''
'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)            # [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
'''
'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end = ' ')
    print()
'''
# ORDENANDO
'''
from operator import itemgetter

raking = list()
ranking = sorted(dado.items(), key = itemgetter(1), reverse = True)
'''