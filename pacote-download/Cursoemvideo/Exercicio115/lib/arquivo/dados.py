from lib.interface.menu import *
from colorama import Fore


def existearquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(Fore.RED, 'Houve um problema ao tentar criar o arquivo.', Fore.RESET)
    else:
        print(Fore.BLUE, f'Arquivo {nome} criado com sucesso!', Fore.RESET)


def lerarquivo(nome):
    try:
        arquivo = open(nome, 'r')
    except:
        print(Fore.RED, 'ERRO ao ler o arquivo!', Fore.RESET)
    else:
        cab('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()
    
    
def adicionar(arquivo, nome ='desconhecido', idade = 0):
    cab('NOVO CADASTRO')
    try:
        a = open(arquivo, 'at')
    except:
        print(Fore.RED, 'ERRO na abertura do arquivo!', Fore.RESET)
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(Fore.RED, 'ERRO na escrita do arquivo!', Fore.RESET)
        else:
            print(f'{Fore.YELLOW}Novo registro de {nome} adicionado.{Fore.RESET}')
            a.close()


def sair():
    cab('Saindo do sistema... Até logo!')