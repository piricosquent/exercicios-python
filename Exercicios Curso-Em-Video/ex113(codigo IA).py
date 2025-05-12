def cor(codigo):
    # Dicionário com códigos ANSI para colorir texto no terminal.
    # Nome do dicionário "codigos" é claro e autoexplicativo.
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
    # get() evita erro caso o código não esteja no dicionário. Default = Reset
    return codigos.get(codigo, "\033[0m")

def ler_entrada(tipo):
    # tipo: define se será "inteiro" ou "real", tornando a função genérica
    while True:
        entrada = input(f'Digite um número {tipo}: ')

        # Limpa espaços e verifica se a string está vazia.
        if entrada.strip() == "":
            print(f'{cor(1)}Erro: entrada vazia. Tente novamente.{cor(0)}')
            continue

        try:
            # Converte com base no tipo: evita duplicar código.
            return int(entrada) if tipo == "inteiro" else float(entrada)
        except (ValueError):
            print(f'{cor(1)}Número inválido. Tente novamente.{cor(0)}')

def ler_numeros():
    # Encapsula a chamada de entrada para tornar a lógica principal mais limpa.
    inteiro = ler_entrada("inteiro")
    real = ler_entrada("real")
    return [inteiro, real]


# Execução principal do programa
numeros = ler_numeros()
print(f'Inteiro: {numeros[0]}\nReal: {numeros[1]:.2f}')
