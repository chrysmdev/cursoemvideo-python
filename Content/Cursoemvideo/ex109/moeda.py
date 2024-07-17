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
    return (f'{moeda} {preço:.2f}').replace('.', ',')