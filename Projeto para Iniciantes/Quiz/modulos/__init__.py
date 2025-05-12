import time

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

def dormir(a = 0.6):
    time.sleep(a)

def pergunta(enunciado, a, b, c, d):
    print(f'{enunciado.title()}')
    print(f'(A) {a}.')
    print(f'(B) {b}.')
    print(f'(C) {c}.')
    print(f'(D) {d}.')
    resp = input(f'{cor(2)}Resposta [A/B/C/D]: {cor(0)}')
    return resp.upper()

def verificacao(gabarito, resp):
    if resp == gabarito.upper():
        dormir()
        print("✅ Resposta correta!")
        return 1
    else:
        dormir()
        print(f"❌ Resposta incorreta. A resposta correta era: {gabarito.upper()}")
        return 0

def linhas(num=30):
    print('-'*num)

def cabecalho(txt, num=30):
    linhas(num)
    print(txt.center(num))
    linhas(num)
