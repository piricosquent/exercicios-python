from time import sleep

import sys

def dormir(num = 0.5):
    sleep(num)

def linhas(num=30):
    print('-'*num)

def cabecalho(txt, num=30, flush=True):
    linhas()
    print(txt.center(num))
    linhas()

def opcao_1():
    cabecalho('Opção 1')

def opcao_2():
    cabecalho('Opção 2')

def opcao_3():
    cabecalho('Saindo do sistema... Até logo...')

def cor(codigo):
    codigos = {
        0: "\033[0m",     # Reset
        1: "\033[31m",    # Vermelho
        2: "\033[32m",    # Verde
        3: "\033[33m",    # Amarelo
        4: "\033[34m",    # Azul
        5: "\033[35m",    # Magenta
        6: "\033[36m",    # Ciano
        7: "\033[37m",    # Branco
        8: "\033[1m",     # Negrito
        9: "\033[4m",     # Sublinhado
    }

    return codigos.get(codigo, "\033[0m")

def ler_int(txt):
    while True:
        numero_lido = input(f'Digite {txt}:').strip()
        if numero_lido == "":
            print(f'{cor(1)}Erro: entrada vazia. Tente novamente.{cor(0)}')
        else:
            try:
                numero_inteiro = int(numero_lido)
                return numero_inteiro
                break
            except:
                print(f'{cor(1)}Número inválido. Tente novamente.{cor(0)}')


def menu(lista):
    c = 1
    for v in lista:
        print(f'{cor(3)} {c} - {cor(4)}{v}{cor(0)}')
        c += 1
        dormir()
    escolha = input((f'{cor(2)}Sua escolha:{cor(0)}'))
    return escolha