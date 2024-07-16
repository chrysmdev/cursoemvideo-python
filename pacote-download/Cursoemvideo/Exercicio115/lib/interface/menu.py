from time import sleep
from colorama import Fore

def cab(txt):
    print('-' * 40)
    print(f'{txt:^40}')
    print('-' * 40)
    
      
def menu(lista):
    cab('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{Fore.YELLOW}{c}{Fore.RESET} - {Fore.CYAN}{item}{Fore.RESET}')
        c += 1
    print('-' * 40)
    opc = validador(f'{Fore.YELLOW}Sua opção: {Fore.RESET}')
    return opc
    

def validador(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(Fore.RED, f'ERRO!!! Não é um número válido, digite novamente.', Fore.RESET)
            continue
        except (KeyboardInterrupt):
            print(Fore.RED, 'Usuário preferiu não digitar esse número.', Fore.RESET)
            return 0
        else:
            if valor in (1,2,3):
                return valor
            else:
                print(Fore.RED, f'ERRO!!! {valor} não é um número inteiro válido, digite novamente um valor inteiro de 1 a 3.', Fore.RESET)
            
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!!! Não é um número inteiro válido, digite novamente.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
