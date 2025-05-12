def maior(*num):
    maior_valor = 0
    for v in num:
        print('\033[31m   ', end='')
        print(f' {v}', end='\033[0m')
        if v > maior_valor:
            maior_valor = v
    linhas(f'\033[35m    O maior valor digitado foi\033[34m {maior_valor}\033[0m.')
def linhas(msg):
    print()
    linhas = msg.split('\n')
    tam = max(len(l) for l in linhas) + 4
    print('-' * tam)
    for l in linhas:
        print(f'\033[36m  {l}\033[0m')
    print('-' * tam)


linhas('Os valores digitados foram:')
maior(1, 2, 3, 4, 5)