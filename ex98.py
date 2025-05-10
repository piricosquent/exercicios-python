import time
def linha(msg):
    linhas = msg.split('\n')
    tam = max(len(l) for l in linhas) + 4
    print('-' * tam)
    for l in linhas:
        print(f'{l}'.center(tam))
    print('-' * tam)
def contador(inicio, fim, passo):
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=' ', flush=True)
            inicio += passo
            time.sleep(0.2)
        print('\n')
    else:
        c = abs(passo)
        while fim <= inicio:
            print(inicio, end=' ', flush=True)
            inicio += -c
            time.sleep(0.2)
        print('\n')



boasvindas = 'CONTAGEM\nCOM PYTHON'
linha(boasvindas)
contador(0, 10, 1)
contador(10, 0, 1)
inicio = int(input('A contagem vai de:'))
fim = int(input('Até:'))
passo = int(input('Ao passo de:'))
msgfinal = 'HA HA HA'
linha(msgfinal)
time.sleep(0.5)
contador(inicio, fim, passo)