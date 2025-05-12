def fatorial(num, op=0):
    """
    -> calcula o valor do fatorial de um número
    :param num: define o número
    :param op: com valor, imprime o cálculo, sem valor imprime somente o resultado
    :return: retorna o valor do fatorial ou o cálculo completo
    """
    fat = 1
    for v in range(num, 0, -1):
        fat *= v
    if op == 0:
        print(f'O fatorial de {num} é {fat}.')
    if op != 0:
        for v in range(num, 1, -1):
            print(v, end=' x ')
        print(f'1 = {fat}')





fatorial(5)
fatorial(5, 'sim')