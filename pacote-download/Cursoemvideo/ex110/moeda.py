# aumentar(), diminuir(), dobro() e metade().

def dobro(preço = 0, m = False):
    res = preço * 2
    if m:
        return moeda(res)
    return res


def metade(preço = 0, m = False):
    res = preço / 2
    if m:
        return moeda(res)
    return res


def aumentar(preço = 0, taxa = 0, m = False):
    res = preço + (preço * taxa / 100)
    if m:
        return moeda(res)
    return res


def diminuir(preço = 0, taxa = 0, m = False):
    res = preço - (preço * taxa /100)
    if m:
        return moeda(res)
    return res

def moeda(preço = 0, moeda = 'R$'):
    return (f'{moeda}{preço:>7.2f}').replace('.', ',')


def resumo(preço = 0, mais = 0, menos = 0):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{mais}% de aumento: \t{aumentar(preço, mais, True)}')
    print(f'{menos}% de redução: \t{diminuir(preço, menos, True)}')
    print('-' * 35)