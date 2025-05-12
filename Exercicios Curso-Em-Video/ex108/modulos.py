def aumento(num, taxa):
    r = num*(1 + taxa*0.01)
    return formatacao(r)


def diminuição(num, taxa):
    r = num*(1 - taxa*0.01)
    return formatacao(r)


def dobro(num):
    r = num*2
    return formatacao(r)


def metade(num):
    r = num*0.5
    return formatacao(r)


def formatacao(num):
    reais = int(num)
    centavos = int(round((num - reais) * 100))
    return f'R${reais},{centavos:02d}'

