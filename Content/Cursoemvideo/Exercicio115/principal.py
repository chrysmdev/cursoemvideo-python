from lib.interface.menu import *
from lib.arquivo.dados import *
from time import sleep

arq = 'cadastro.txt'

if not existearquivo(arq):
    criararquivo(arq)
    
while True:
    opção = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opção == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerarquivo(arq)
    elif opção == 2:
        # Opção de cadastrar uma nova pessoa e sua idade.
        cab('NOVO CADASTRO')
        nome = str(input(f'{Fore.YELLOW}Nome: {Fore.RESET}')).strip()
        idade = leiaInt(f'{Fore.YELLOW}Idade: {Fore.RESET}')
        adicionar(arq, nome, idade)
    elif opção == 3:
        # Opção de sair do sistema.
        sair()
        break
    sleep(1)

