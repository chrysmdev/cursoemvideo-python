# AULA 11

# ANSI  escape sequence
# \033[0;30;41m
# 1° codigo =  style    0(none)  1(bold)  4(underline)  7(negative)
# 2° codigo =  text     30(white)  31(red)  32(green)  33(yellow)  34(blue)  35(magenta)  36(cyan)  37(gray)
# 3° codigo = back      40(white)  41(red)  42(green)  43(yellow)  44(blue)  45(magenta)  46(cyan)  47(gray)

# print('\033[7;31;46mOlá, Mundo!\033[m')

'''
cores = {'limpa' : '\033[m', 
        'azul' : '\033[34m', 
        'amarelo' : '\033[33m', 
        'pretobranco' : '\033[7;30m'}
print(f'{cores['azul']}Olá, Mundo!{cores['limpa']}')
'''
s = 'prova de python'
print(len(s))