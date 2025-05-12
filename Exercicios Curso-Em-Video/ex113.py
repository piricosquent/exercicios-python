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

def ler_numero():
    while True:
        primeiro_numero_lido = input('Digite um número inteiro:').strip()
        if primeiro_numero_lido == "":
            print(f'{cor(1)}Erro: entrada vazia. Tente novamente.{cor(0)}')
        else:
            try:
                numero_inteiro = int(primeiro_numero_lido)
                break
            except:
                print(f'{cor(1)}Número inválido. Tente novamente.{cor(0)}')
    while True:
        segundo_numero_lido = input('Agora, digite um número real:').strip()
        if segundo_numero_lido == "":
            print(f'{cor(1)}Erro: entrada vazia. Tente novamente.')
        else:
            try:
                numero_real = float(segundo_numero_lido)
                break
            except:
                print(f'{cor(1)}Número inválido. Tente novamente.{cor(0)}')
    return [numero_inteiro, numero_real]


resultados = ler_numero()
print(f'Inteiro: {resultados[0]}\nReal: {resultados[1]:.2f}')


